# supervisor가 노드 판단하는 로직

# supervisor가 몇 번까지 고르는지 상한값
MAX_TURNS = 4

# 예시 규칙 : 질문에 아래 낱말이 있으면 초안까지
DRAFT_WORDS = ("신청서", "초안")


# 상태를 보고 다음 작업 노드를 고르기
def pick_worker(state: dict) -> str:
    if state.get("turns", 0) >= MAX_TURNS:
        return "finish"
    if "sources" not in state:
        return "search"
    if any((w in state["question"] for w in DRAFT_WORDS)) and state.get("sources") and ("draft" not in state):
        return "draft"
    return "finish"
