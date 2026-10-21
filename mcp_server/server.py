from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT / "backend"))

from app.core.logging import setup_logging

# 우리 로그와 우리가 부른 라이브러리의 로그를 표준 오류로 내보내기
setup_logging(stream=sys.stderr)

# 진짜 출구를 변수에 담아두기
_PROTOCOL_OUT = sys.stdout

# 사용자가 실수로 print 해도 표준 오류로 나가도록 처리
sys.stdout = sys.stderr

# 지정된 MCP 프로토콜 버전 중 선택
PROTOCOL_VERSION = "2024-11-05"

SERVER_INFO = {"name": "agent-practice", "version": "1.0.0"}
CAPABILITIES: dict = {}


# 응답 메세지 한줄을 stdout에 작성하는 함수
def respond(msg_id, result=None, error=None) -> None:
    payload = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        payload["error"] = error
    else:
        payload["result"] = result
    _PROTOCOL_OUT.write(json.dumps(payload, ensure_ascii=False) + "\n")  # 한글을 코드로 바꾸지 않겠다.
    _PROTOCOL_OUT.flush()


# handshake 기능
def on_initialize(msg_id, params: dict) -> None:
    respond(
        msg_id,
        {
            "protocalVersion": PROTOCOL_VERSION,
            "capabilities": CAPABILITIES,
            "serverInfo": SERVER_INFO,
        },
    )


# ping
def on_ping(msg_id, params: dict) -> None:
    respond(msg_id, {})


# 메서드 이름 : 처리 함수 형태로 도구 저장
METHODS = {"initialize": on_initialize, "ping": on_ping}


# 요청 한 건을 처리 함수에 넘겨주는 함수
def handle(message: dict) -> None:
    msg_id = message.get("id")
    if msg_id is None:
        return
    fn = METHODS.get(message.get("method"))
    if fn is None:
        respond(msg_id, error={"code": -32601, "message": f"지원하지 않는 매서드: {message.get('method')}"})
        return
    fn(msg_id, message.get("params") or {})


def main() -> int:
    print("[agent-practice MCP] 메서드" + " · ".join(METHODS), file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        handle(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
