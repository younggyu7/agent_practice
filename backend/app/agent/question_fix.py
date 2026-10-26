FIX_WORDS: dict[str, str] = {
    "호텔비": "숙박비",
    "밥값": "식비",
    "기차표": "교통비",
}


# 질문을 위 사전을 참고하여 한번 고쳐주는 함수(노드)
def fix_question(state: dict) -> dict:
    q = state.get("query") or state["question"]  # 질문을 꺼내기
    for old, new in FIX_WORDS.items():
        q = q.replace(old, new)
    return {"query": q, "fixes": state.get("fixed", 0) + 1}  # 고친 질문, 고친 횟수 반환


# 고치는 횟수 상한값 지정
from app.agent.patterns import route_after_search

# 질문 고치기 2번까지 상한으로 지정
MAX_FIXES = 3


def route_with_fixes(state: dict) -> str:
    if route_after_search(state) == "found":  # found or insufficient 반환
        return "found"
    return "fix" if state.get("fixes", 0) < MAX_FIXES else "insufficient"  # fix or found or insufficient 반환
