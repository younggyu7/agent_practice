# 실행 번호 run_id 만들어주는 모듈

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Run

RUN_START = 8821  # 1부터 시작하면 자릿수가 바뀌면 줄이 어긋남


# 다음 run_id 번호 만들어 주는 함수 : RUN-8821 형태로 리턴
def next_run_id(session: Session) -> str:
    used = session.scalars(select(Run.id)).all()

    numbers = [RUN_START - 1]
    for run_id in used:
        tail = run_id.removeprefix("RUN-")
        if tail.isdigit():
            numbers.append(int(tail))

    return f"RUN-{max(numbers) + 1:04d}"
