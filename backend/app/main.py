from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.documents import router as documents_router
from app.core.exceptions import AgentError
from contextlib import asynccontextmanager
from app.core.logging import setup_logging


# lifespan 함수 정의 : FastApi에서 lifespan은 무조건 비동기로 하라고 정의되어있음
@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield


app = FastAPI(
    title="사내 AI 에이전트",
    version="0.1.0",
    lifespan=lifespan,
)


# 서버 상태 확인용 API
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# 라우터 연결
app.include_router(
    documents_router,
    prefix="/api/v1",
)


# 에외 처리 규약에서 함수 정의시 비동기로 하라고 정의되어있음(framework에서 정의됨)
@app.exception_handler(AgentError)
async def handle_agent_error(
    request: Request,
    exc: AgentError,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.code,
            "message": str(exc),
            "detail": None,
        },
    )
