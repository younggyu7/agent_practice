from collections.abc import Callable

from langgraph.graph import END, START, StateGraph

from app.agent.patterns import Step
from app.agent.state import WorkflowState

"""
START -> search -> pick(state) ----- "found"        -> found        -> END
                               |
                                ---- "insufficient" -> insufficient -> END
"""


# search -> (pick이 고른 갈래) -> END
def build_graph(search: Step, routes: dict[str, Step], pick: Callable[[dict], str]):
    g = StateGraph(WorkflowState)  # 상태 선언
    g.add_node("search", search)  # 첫 단계 노드로 등록 : 검색
    for name, step in routes.items():
        g.add_node(name, step)
        g.add_edge(name, END)
    g.add_edge(START, "search")  # 시작 -> search부터 실행
    g.add_conditional_edges("search", pick, {name: name for name in routes})
    return g.compile()  # 그래프 생성


# 되돌아가는 선 추가
from langgraph.types import RetryPolicy
from app.agent.state import LoopState


def build_loop_graph(
    search: Step,
    fix: Step,
    routes: dict[str, Step],
    pick: Callable[[dict], str],
    *,
    search_retry: RetryPolicy | None = None,
    fix_retry: RetryPolicy | None = None,
    checkpointer=None,
):
    g = StateGraph(LoopState)
    g.add_node("search", search, retry_policy=search_retry)
    g.add_node("fix", fix, retry_policy=fix_retry)
    for name, step in routes.items():
        g.add_node(name, step)
        g.add_node(name, END)

    g.add_edge(START, "search")
    g.add_conditional_edges("search", pick, {"fix": "fix", **{name: name for name in routes}})
    g.add_edge("fix", "search")
    return g.compile(checkpointer=checkpointer)


# 승인 그래프, 게이트
from langgraph.types import interrupt
from app.agent.state import ApprovalState


# 사람의 결정을 기다리게 하는 함수
def _gate(state: dict) -> dict:
    return {"decision": interrupt({"text": state["text"]})}


# 승인 그래프 : draft -> gate(멈춤) -> 승인이면 send -> END
def build_approval_graph(draft: Step, send: Step, *, checkpointer):
    if checkpointer is None:
        raise ValueError("승인 그래프는 저장소가 있어야 멈췄다 이어 간다. checkpointer를 넘기세요.")

    g = StateGraph(ApprovalState)
    g.add_node("draft", draft)
    g.add_node("gate", _gate)
    g.add_node("send", send)

    g.add_edge(START, "draft")
    g.add_edge("draft", "gate")

    def pick(state: dict) -> str:
        return "send" if state["decision"].get("approved") else "end"

    routes = {"send": "send", "end": END}
    g.add_conditional_edges("gate", pick, routes)
    g.add_edge("send", END)

    return g.compile(checkpointer=checkpointer)
