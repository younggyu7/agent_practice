# FastApi 파일별 함수·클래스 상세 명세

확인일: 2026-09-29

## 읽는 방법과 범위

- `venv`, `sandbox`, 캐시, Git 내부는 제외합니다. 프로젝트가 직접 정의한 모든 Python 클래스·함수·메서드·중첩 함수와 lambda를 포함합니다.
- 모든 항목은 `FastApi/...` 경로와 원본 줄 번호를 표시합니다. 같은 이름의 함수도 파일별로 구분합니다.
- 호출·사용 위치는 import 별칭과 재공개를 따라가 정적으로 확인했습니다. 참조에는 타입 표기·상속·콜백 전달도 포함되므로 실제 호출과 구분합니다.
- 객체 타입을 정적으로 확정하지 못한 메서드·속성 접근은 **후보**로 별도 표시합니다. 후보를 실제 실행으로 단정하지 않습니다. 직접 참조가 없더라도 프레임워크가 실행할 수 있습니다.
- 외부 라이브러리 내부의 모든 상속 메서드까지 복제하지 않습니다. 대신 BaseModel·ORM·dataclass 등 자동 제공 메서드와 프로젝트에서의 사용을 설명합니다.
- 타입 표기와 실제 반환 표현식을 함께 적습니다. `None` 반환은 일반 반환값 없음, `yield`는 contextmanager/fixture가 값을 제공하는 별도 동작입니다. 비동기 함수는 await 후의 결과를 읽습니다.
- 기본값의 `Field(...)`/`mapped_column(...)`은 선언 규칙입니다. 데이터가 없다는 뜻의 None과 구분합니다. `.env` 실제 값과 시드 비밀번호 값은 복사하지 않습니다.
- 실제 서버·테스트·DB를 실행한 결과가 아닌 소스 분석입니다. 문서 작성으로 앱 코드를 변경하지 않았습니다.

<details>
<summary><h1>전체 파일 색인</h1></summary>
>
> | 파일 | 클래스 수 | 함수·메서드 수 | lambda 수 |
> | --- | ---: | ---: | ---: |
> | `FastApi/backend/app/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/agent/chain.py` | 0 | 6 | 1 |
> | `FastApi/backend/app/api/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/api/v1/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/api/v1/auth.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/api/v1/chat.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/api/v1/deps.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/api/v1/documents.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/core/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/core/config.py` | 1 | 3 | 0 |
> | `FastApi/backend/app/core/exceptions.py` | 10 | 2 | 0 |
> | `FastApi/backend/app/core/guards.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/core/logging.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/core/security.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/db/init_db.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/migrations/env.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/db/seed.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/db/seed_data.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/db/session.py` | 0 | 4 | 0 |
> | `FastApi/backend/app/integrations/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/integrations/factory.py` | 0 | 2 | 0 |
> | `FastApi/backend/app/integrations/langfuse_client.py` | 0 | 4 | 0 |
> | `FastApi/backend/app/integrations/llm_claude.py` | 1 | 7 | 0 |
> | `FastApi/backend/app/integrations/ports.py` | 2 | 1 | 0 |
> | `FastApi/backend/app/main.py` | 0 | 4 | 0 |
> | `FastApi/backend/app/models/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/models/base.py` | 2 | 0 | 0 |
> | `FastApi/backend/app/models/document.py` | 2 | 3 | 0 |
> | `FastApi/backend/app/models/org.py` | 2 | 2 | 0 |
> | `FastApi/backend/app/models/run.py` | 2 | 0 | 0 |
> | `FastApi/backend/app/models/usage.py` | 1 | 0 | 0 |
> | `FastApi/backend/app/repositories/document_repo.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/repositories/user_repo.py` | 0 | 1 | 0 |
> | `FastApi/backend/app/schemas/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/schemas/auth.py` | 2 | 0 | 0 |
> | `FastApi/backend/app/schemas/chat.py` | 4 | 0 | 0 |
> | `FastApi/backend/app/schemas/common.py` | 2 | 0 | 0 |
> | `FastApi/backend/app/schemas/document.py` | 2 | 0 | 0 |
> | `FastApi/backend/app/services/__init__.py` | 0 | 0 | 0 |
> | `FastApi/backend/app/services/auth_service.py` | 0 | 3 | 0 |
> | `FastApi/backend/app/services/chat_service.py` | 0 | 5 | 0 |
> | `FastApi/backend/app/services/document_service.py` | 0 | 4 | 0 |
> | `FastApi/backend/app/services/ids.py` | 0 | 1 | 0 |
> | `FastApi/backend/tests/conftest.py` | 0 | 2 | 0 |
> | `FastApi/backend/tests/test_chat_golden.py` | 1 | 5 | 1 |
> | `FastApi/backend/tests/test_core_config.py` | 0 | 2 | 0 |
> | `FastApi/backend/tests/test_exceptions.py` | 0 | 3 | 0 |
> | `FastApi/backend/tests/test_guards.py` | 0 | 5 | 0 |
> | `FastApi/backend/tests/test_health.py` | 0 | 3 | 0 |
> | `FastApi/backend/tests/test_layers.py` | 0 | 9 | 0 |
> | `FastApi/frontend/app.py` | 0 | 2 | 0 |
> | `FastApi/frontend/core/__init__.py` | 0 | 0 | 0 |
> | `FastApi/frontend/core/api_client.py` | 1 | 6 | 0 |
> | `FastApi/frontend/core/router.py` | 0 | 2 | 0 |
> | `FastApi/frontend/core/session.py` | 0 | 6 | 0 |
> | `FastApi/frontend/ui/__init__.py` | 0 | 0 | 0 |
> | `FastApi/frontend/ui/badge.py` | 0 | 4 | 0 |
> | `FastApi/frontend/ui/card.py` | 0 | 9 | 0 |
> | `FastApi/frontend/ui/chart.py` | 0 | 5 | 0 |
> | `FastApi/frontend/ui/metric.py` | 0 | 1 | 0 |
> | `FastApi/frontend/ui/source.py` | 0 | 2 | 0 |
> | `FastApi/frontend/ui/status.py` | 0 | 3 | 0 |
> | `FastApi/frontend/ui/table.py` | 0 | 5 | 0 |
> | `FastApi/frontend/ui/theme.py` | 0 | 2 | 0 |
> | `FastApi/frontend/ui_kit_demo.py` | 0 | 0 | 0 |
> | `FastApi/frontend/views/__init__.py` | 0 | 0 | 0 |
> | `FastApi/frontend/views/documents.py` | 0 | 4 | 0 |
> | `FastApi/frontend/views/login.py` | 0 | 1 | 0 |
>
</details>

## 토글 사용법

- **폴더·파일:** 제목 1 수준의 토글입니다. 파일은 전체 경로로 표시합니다.
- **클래스·함수·메서드:** 제목 2 수준의 토글입니다. 번호는 파일마다 1부터 시작합니다.
- 예: `1. [클래스] ClaudeLLM` 안에 `1.1. [초기화 메서드] ClaudeLLM.__init__`, `1.2. [인스턴스 메서드] ClaudeLLM._call`이 들어갑니다.
- 클래스에 속하지 않는 함수는 **독립 함수**, 함수 안에 정의된 함수는 **중첩 함수**로 구분합니다.
- 각 토글은 기본적으로 접혀 있습니다. HTML details/summary와 제목을 지원하는 Markdown 뷰어에서 펼칠 수 있습니다.

<details>
<summary><h1>[폴더] FastApi</h1></summary>
>
> <details>
> <summary><h1>[파일] FastApi/.env</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** FastApi/backend/app/core/config.py의 Settings가 읽는 환경설정입니다. 실제 값은 문서에 싣지 않습니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/FUNCTION_CLASS_REFERENCE.md</h1></summary>
> >
> > 현재 문서입니다. 함수·클래스를 실행하지 않습니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/PROJECT_STRUCTURE.md</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** 사람이 읽는 폴더·기능 구조 안내입니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/app.db</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** SQLite 데이터 파일입니다. FastApi/backend/app/db/session.py의 get_engine에서 해당 URL을 선택한 경우 사용됩니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/docker-compose.yml</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** Docker Compose가 PostgreSQL·Langfuse 서비스를 구성할 때 읽습니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/netstat</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** 저장된 터미널 출력이며 애플리케이션 함수에서 사용하는 참조를 확인하지 못했습니다.
> >
> </details>
>
> <details>
> <summary><h1>[파일] FastApi/pyproject.toml</h1></summary>
> >
> > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > - **사용 위치:** pytest가 Python 검색 경로와 테스트 위치 설정을 읽습니다.
> >
> </details>
>
> <details>
> <summary><h1>[폴더] FastApi/backend</h1></summary>
> >
> > <details>
> > <summary><h1>[파일] FastApi/backend/alembic.ini</h1></summary>
> > >
> > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > - **사용 위치:** Alembic CLI가 읽고 FastApi/backend/app/db/migrations/env.py의 실행 환경을 설정합니다.
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/backend/app</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/app/__init__.py</h1></summary>
> > > >
> > > > 직접 정의한 함수·클래스: **없음**.
> > > >
> > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/app/main.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `lifespan`, `health`, `handle_agent_error`, `handle_validation_error`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] lifespan</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/app/main.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/app/main.py:17`
> > > > > - **역할·로직:** FastAPI 시작 시 로깅을 설정하고 yield로 서버 실행에 제어를 넘깁니다.
> > > > > - **데코레이터:** `asynccontextmanager`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `app` | `FastAPI` | `필수` | `위치/키워드` | FastAPI 애플리케이션 객체 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `타입 표기 없음`
> > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > - 호출하면 컨텍스트 매니저를 반환합니다. with/async with 진입 시 아래 값을 제공하고, 블록 종료 시 yield 뒤 정리 코드를 실행합니다.
> > > > > - 제공 값: `(yield)`
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > async def lifespan(app: FastAPI):
> > > > > >     setup_logging()
> > > > > >     yield
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastApi/backend/app/main.py에서 FastAPI(lifespan=lifespan)에 등록합니다. 서버 수명주기에 따라 실행됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/app/main.py:25` — `모듈 실행부` / 참조·타입·콜백 등
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] health</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/app/main.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/app/main.py:31`
> > > > > - **역할·로직:** 서버 상태 확인용 status=ok 응답을 만듭니다.
> > > > > - **데코레이터:** `app.get('/health')`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return {'status': 'ok'}
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def health() -> dict:
> > > > > >     return {"status": "ok"}
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] handle_agent_error</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/app/main.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/app/main.py:52`
> > > > > - **역할·로직:** 프로젝트 예외의 상태 코드와 메시지를 JSON HTTP 응답으로 바꿉니다.
> > > > > - **데코레이터:** `app.exception_handler(AgentError)`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `request` | `Request` | `필수` | `위치/키워드` | 현재 HTTP 요청 객체 |
> > > > > | `exc` | `AgentError` | `필수` | `위치/키워드` | 처리할 예외 객체 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `JSONResponse`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return JSONResponse(status_code=exc.status_code, content={'code': exc.code, 'message': str(exc), 'detail': None})
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > async def handle_agent_error(
> > > > > >     request: Request,
> > > > > >     exc: AgentError,
> > > > > > ) -> JSONResponse:
> > > > > >     return JSONResponse(
> > > > > >         status_code=exc.status_code,
> > > > > >         content={
> > > > > >             "code": exc.code,
> > > > > >             "message": str(exc),
> > > > > >             "detail": None,
> > > > > >         },
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastApi/backend/app/main.py에서 FastAPI 예외 핸들러로 등록되어 해당 예외 발생 시 프레임워크가 호출합니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] handle_validation_error</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/app/main.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/app/main.py:68`
> > > > > - **역할·로직:** 요청 검증 오류에서 필드 이름을 추려 값 노출 없이 422 응답을 만듭니다.
> > > > > - **데코레이터:** `app.exception_handler(RequestValidationError)`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `request` | `Request` | `필수` | `위치/키워드` | 현재 HTTP 요청 객체 |
> > > > > | `exc` | `RequestValidationError` | `필수` | `위치/키워드` | 처리할 예외 객체 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `JSONResponse`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return JSONResponse(status_code=422, content={'code': 'validation_failed', 'message': f'입력값을 확인하세요 — {fields}', 'detail': None})
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > async def handle_validation_error(
> > > > > >     request: Request, exc: RequestValidationError
> > > > > > ) -> JSONResponse:
> > > > > >     # exc.errors() 에는 사용자가 보낸 값이 통째로 들어 있다. 필드 이름만 돌려주고 값은 감춘다.
> > > > > >     fields = ", ".join(
> > > > > >         ".".join(str(p) for p in e["loc"][1:]) or "요청 본문" for e in exc.errors()
> > > > > >     )
> > > > > >     return JSONResponse(
> > > > > >         status_code=422,
> > > > > >         content={
> > > > > >             "code": "validation_failed",
> > > > > >             "message": f"입력값을 확인하세요 — {fields}",
> > > > > >             "detail": None,
> > > > > >         },
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastApi/backend/app/main.py에서 FastAPI 예외 핸들러로 등록되어 해당 예외 발생 시 프레임워크가 호출합니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/agent</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/agent/chain.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `load_prompt`, `build_prompt`, `build_result_chain`, `build_answer_chain`, `build_parsed_chain`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] load_prompt</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:22`
> > > > > > - **역할·로직:** 이름에 해당하는 Markdown 프롬프트를 읽고 공백을 정리합니다. 파일이 없으면 FileNotFoundError를 발생시킵니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return path.read_text(encoding='utf-8').strip()
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def load_prompt(name: str) -> str:
> > > > > > >     # name : 확장자를 뺀 md 파일명 "answer_system"
> > > > > > >     path = PROMPT_DIR / f"{name}.md"
> > > > > > >     if not path.is_file():
> > > > > > >         raise FileNotFoundError(f"프롬프트 파일을 찾을 수 없습니다: {path}")
> > > > > > >     return path.read_text(encoding="utf-8").strip()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:32` — `build_prompt` / 직접 호출
> > > > > > - `FastApi/backend/app/agent/chain.py:74` — `build_parsed_chain` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] build_prompt</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:30`
> > > > > > - **역할·로직:** 시스템 메시지와 {question} 입력 칸으로 ChatPromptTemplate을 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `system_prompt` | `str \| None` | `None` | `키워드 전용` | 시스템 프롬프트; 생략 시 기본 파일 사용 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `ChatPromptTemplate`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return ChatPromptTemplate.from_messages([SystemMessage(content=system_prompt), ('human', '{question}')])
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def build_prompt(*, system_prompt: str | None = None) -> ChatPromptTemplate:
> > > > > > >     # system_prompt : 시스템 메세지 본문. 외부에서 주지 않으면 answer_system 으로 처리 
> > > > > > >     system_prompt = system_prompt or load_prompt("answer_system") 
> > > > > > >     return ChatPromptTemplate.from_messages(
> > > > > > >         [
> > > > > > >             SystemMessage(content=system_prompt),
> > > > > > >             ("human", "{question}")
> > > > > > >         ]
> > > > > > >     )
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:51` — `build_result_chain` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] build_result_chain</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:41`
> > > > > > - **역할·로직:** 프롬프트와 포트 호출을 Runnable로 연결합니다. 체인을 만들며, 여기서 모델 호출을 실행하지는 않습니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `llm` | `LLMPort` | `필수` | `위치/키워드` | LLMPort 규약을 만족하는 어댑터 객체 |
> > > > > > | `system_prompt` | `str \| None` | `None` | `키워드 전용` | 시스템 프롬프트; 생략 시 기본 파일 사용 |
> > > > > > | `contexts` | `list[dict] \| None` | `None` | `키워드 전용` | 모델에게 전달할 근거 문서 dict 목록 |
> > > > > > | `user` | `dict \| None` | `None` | `키워드 전용` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Runnable`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return prompt | llm_step
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def build_result_chain(
> > > > > > >         llm: LLMPort, 
> > > > > > >         *,
> > > > > > >         system_prompt: str | None = None, 
> > > > > > >         contexts: list[dict] | None = None, 
> > > > > > >         user: dict | None = None, 
> > > > > > > ) -> Runnable:
> > > > > > >     # llm : LLMPort를 만족하는 어댑터. 추후 LLMPort 규격만 맞으면 다른 API 모델 사용가능 
> > > > > > >     # contexts : 근거 목록 
> > > > > > >     # user : 질문한 사람 
> > > > > > >     prompt = build_prompt(system_prompt=system_prompt)
> > > > > > >     port_contexts: list[dict] = [] if contexts is None else contexts
> > > > > > >     port_user: dict = {} if user is None else user 
> > > > > > >
> > > > > > >     # ChatPromptTemplate -> LLMResult 연결 다리  
> > > > > > >     def call_port(value) -> LLMResult:
> > > > > > >         messages = value.to_messages()
> > > > > > >         question = "\n\n".join(str(m.content) for m in messages)
> > > > > > >         return llm.answer(question=question, contexts=port_contexts, user=port_user)
> > > > > > >
> > > > > > >     llm_step = RunnableLambda(call_port).with_config(run_name="LLMPort")
> > > > > > >
> > > > > > >     return prompt | llm_step
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:68` — `build_answer_chain` / 직접 호출
> > > > > >
> > > > > > **이 함수 안의 함수**
> > > > > >
> > > > > > - 3.1 `build_result_chain.call_port`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>3.1. [중첩 함수] build_result_chain.call_port</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > > >
> > > > > > > **소속 함수:** `build_result_chain`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:56`
> > > > > > > - **역할·로직:** 프롬프트 메시지들의 본문을 문자열로 합쳐 주입된 llm.answer()에 전달합니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `value` | `타입 표기 없음` | `필수` | `위치/키워드` | 변환할 값; call_port에서는 프롬프트 값 객체, score에서는 점수 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `LLMResult`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return llm.answer(question=question, contexts=port_contexts, user=port_user)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def call_port(value) -> LLMResult:
> > > > > > > >         messages = value.to_messages()
> > > > > > > >         question = "\n\n".join(str(m.content) for m in messages)
> > > > > > > >         return llm.answer(question=question, contexts=port_contexts, user=port_user)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastApi/backend/app/agent/chain.py의 build_result_chain에서 RunnableLambda(call_port)로 등록합니다. 반환된 체인을 실행할 때 호출됩니다. 현재 FastApi/backend/app/services/chat_service.py에서는 이 체인을 사용하지 않습니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/agent/chain.py:61` — `build_result_chain` / 참조·타입·콜백 등
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [독립 함수] build_answer_chain</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:66`
> > > > > > - **역할·로직:** LLMResult를 반환하는 체인 뒤에 text 추출 단계를 붙입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `llm` | `LLMPort` | `필수` | `위치/키워드` | LLMPort 규약을 만족하는 어댑터 객체 |
> > > > > > | `**kwargs` | `타입 표기 없음` | `0개 이상` | `추가 키워드 인자` | 하위 함수에 전달할 추가 키워드 옵션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Runnable`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return build_result_chain(llm, **kwargs) | RunnableLambda(lambda r: r.text)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def build_answer_chain(llm: LLMPort, **kwargs) -> Runnable:
> > > > > > >     # 결과가 있으면 텍스트만 추출해서 runnable 타입으로 리턴 
> > > > > > >     return build_result_chain(llm, **kwargs) | RunnableLambda(lambda r: r.text)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:76` — `build_parsed_chain` / 직접 호출
> > > > > >
> > > > > > **이 함수 안의 함수**
> > > > > >
> > > > > > - 4.1 `lambda 1`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>4.1. [익명 함수] lambda 1</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > > >
> > > > > > > **소속 함수:** `build_answer_chain`
> > > > > > >
> > > > > > > - **파일:** `FastApi/backend/app/agent/chain.py:68`
> > > > > > >   - 매개변수: `r`
> > > > > > >   - 반환: `r.text`
> > > > > > >   - 로직: 표현식을 계산해 그대로 반환합니다.
> > > > > > >   - 사용 위치: `FastApi/backend/app/agent/chain.py`의 `build_answer_chain`에서 `RunnableLambda(lambda r: r.text)`에 전달됩니다.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>5. [독립 함수] build_parsed_chain</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/agent/chain.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/agent/chain.py:71`
> > > > > > - **역할·로직:** 출력 형식 지침을 프롬프트에 추가하고 지정한 Pydantic 모델로 파싱하는 체인을 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `llm` | `LLMPort` | `필수` | `위치/키워드` | LLMPort 규약을 만족하는 어댑터 객체 |
> > > > > > | `schema` | `type` | `필수` | `키워드 전용` | 결과를 검증할 Pydantic 모델 클래스 |
> > > > > > | `**kwargs` | `타입 표기 없음` | `0개 이상` | `추가 키워드 인자` | 하위 함수에 전달할 추가 키워드 옵션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Runnable`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return build_answer_chain(llm, system_prompt=system_prompt, **kwargs) | parser
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def build_parsed_chain(llm: LLMPort, *, schema: type, **kwargs) -> Runnable:
> > > > > > >     # schema : 결과를 담을 pydantic 모델 
> > > > > > >     parser = PydanticOutputParser(pydantic_object=schema)
> > > > > > >     base = kwargs.pop("system_prompt", None) or load_prompt("answer_system")
> > > > > > >     system_prompt = f"{base}\n\n{parser.get_format_instructions()}"
> > > > > > >     return build_answer_chain(llm, system_prompt=system_prompt, **kwargs) | parser
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[폴더] FastApi/backend/app/agent/prompts</h1></summary>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/agent/prompts/answer_system.md</h1></summary>
> > > > > >
> > > > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > > > - **사용 위치:** FastApi/backend/app/integrations/llm_claude.py의 _load_prompt와 FastApi/backend/app/agent/chain.py의 load_prompt가 읽습니다.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/api</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/api/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[폴더] FastApi/backend/app/api/v1</h1></summary>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/api/v1/__init__.py</h1></summary>
> > > > > >
> > > > > > 직접 정의한 함수·클래스: **없음**.
> > > > > >
> > > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/api/v1/auth.py</h1></summary>
> > > > > >
> > > > > > **파일 구성**
> > > > > >
> > > > > > - 클래스: 없음
> > > > > > - 파일 수준 함수: `login`, `me`
> > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > >
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1. [독립 함수] login</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/auth.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/auth.py:17`
> > > > > > > - **역할·로직:** LoginIn의 사번과 비밀번호를 인증 서비스에 전달합니다.
> > > > > > > - **데코레이터:** `router.post('/login', response_model=UserOut)`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `body` | `LoginIn` | `필수` | `위치/키워드` | 요청 모델 또는 카드 HTML 본문(타입 참고) |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `dict`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return auth_service.authenticate(body.emp_no, body.password)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def login(body: LoginIn) -> dict: # 사용자가 요청한 데이터는 LoginIn 타입으로 취합 
> > > > > > > >     # 서비스야 로직처리해줘: 사용자가 보내준 emp_no랑 password 줄게, DB가서 일치하는지 확인해봐. 그리고 회원정보 돌려줘. 
> > > > > > > >     return auth_service.authenticate(body.emp_no, body.password)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2. [독립 함수] me</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/auth.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/auth.py:23`
> > > > > > > - **역할·로직:** 요청 헤더의 사번을 확인하고 사용자 조회 서비스를 호출합니다.
> > > > > > > - **데코레이터:** `router.get('/me', response_model=UserOut)`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `x_emp_no` | `Annotated[str \| None, Header()]` | `None` | `위치/키워드` | 요청 헤더로 받은 사번 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `dict`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return auth_service.get_me(x_emp_no)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def me(x_emp_no: Annotated[str | None, Header()] = None) -> dict: # x_emp_no 인증키(사번으로 임시사용) : 헤더 정보로 넘어옴 
> > > > > > > >     # 사번이 존재하지 않으면 예외 발생 
> > > > > > > >     if x_emp_no is None:
> > > > > > > >         raise AuthFailed("로그인이 필요합니다.") 
> > > > > > > >     # 사번이 있으면 회원정보 조회해 리턴 
> > > > > > > >     return auth_service.get_me(x_emp_no)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/api/v1/chat.py</h1></summary>
> > > > > >
> > > > > > **파일 구성**
> > > > > >
> > > > > > - 클래스: 없음
> > > > > > - 파일 수준 함수: `create_message`, `read_run`
> > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > >
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1. [독립 함수] create_message</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/chat.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/chat.py:14`
> > > > > > > - **역할·로직:** 요청의 question을 chat_service.ask()에 전달합니다.
> > > > > > > - **데코레이터:** `router.post('/messages', response_model=AskOut)`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `payload` | `ChatRequest` | `필수` | `위치/키워드` | 검증된 채팅 요청 모델 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `AskOut`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return chat_service.ask(question=payload.question)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def create_message(payload: ChatRequest) -> AskOut:
> > > > > > > >     # 서비스에게 사용자 질문 주고 로직처리 시키기 
> > > > > > > >     return chat_service.ask(question=payload.question)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2. [독립 함수] read_run</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/chat.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/chat.py:20`
> > > > > > > - **역할·로직:** 경로의 run_id로 chat_service.get_run()을 호출합니다.
> > > > > > > - **데코레이터:** `router.get('/runs/{run_id}')`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `run_id` | `str` | `필수` | `위치/키워드` | 질문 한 건의 실행 식별자 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `dict`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return chat_service.get_run(run_id=run_id)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def read_run(run_id: str) -> dict:
> > > > > > > >     # 서비스에게 run_id주고 DB에서 실행 기록 한개 조회해오도록 시키기 
> > > > > > > >     return chat_service.get_run(run_id=run_id)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/api/v1/deps.py</h1></summary>
> > > > > >
> > > > > > **파일 구성**
> > > > > >
> > > > > > - 클래스: 없음
> > > > > > - 파일 수준 함수: `get_request_id`, `get_request_logger`, `get_db`
> > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > >
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1. [독립 함수] get_request_id</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/deps.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/deps.py:21`
> > > > > > > - **역할·로직:** 요청 헤더의 X-Request-ID를 사용하거나 짧은 UUID를 만듭니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `request` | `Request` | `필수` | `위치/키워드` | 현재 HTTP 요청 객체 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `str`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return request.headers.get('X-Request-ID') or uuid.uuid4().hex[:8]
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def get_request_id(request: Request) -> str:
> > > > > > > >     return request.headers.get("X-Request-ID") or uuid.uuid4().hex[:8]
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/api/v1/deps.py:24` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2. [독립 함수] get_request_logger</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/deps.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/deps.py:27`
> > > > > > > - **역할·로직:** 요청 ID를 이름에 포함한 로거를 가져옵니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `request_id` | `RequestIdDep` | `필수` | `위치/키워드` | 요청 식별자 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `logging.Logger`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return get_logger(f'api.req.{request_id}')
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def get_request_logger(request_id: RequestIdDep) -> logging.Logger:
> > > > > > > >     return get_logger(f"api.req.{request_id}")
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/api/v1/deps.py:30` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>3. [독립 함수] get_db</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/deps.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/deps.py:33`
> > > > > > > - **역할·로직:** 요청에 사용할 DB 세션을 yield하고 사용 후 닫습니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > 없음.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `Iterator[Session]`
> > > > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > > > - 호출하면 제너레이터를 반환합니다. pytest/FastAPI 등이 순회하며 아래 값을 받아 사용합니다.
> > > > > > > - 제공 값: `(yield db)`
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def get_db() -> Iterator[Session]:
> > > > > > > >     db = get_sessionmaker()()
> > > > > > > >     try:
> > > > > > > >         yield db
> > > > > > > >     finally:
> > > > > > > >         db.close()
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/api/v1/deps.py:40` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/api/v1/documents.py</h1></summary>
> > > > > >
> > > > > > **파일 구성**
> > > > > >
> > > > > > - 클래스: 없음
> > > > > > - 파일 수준 함수: `list_documents`, `upload_document`, `get_document`
> > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > >
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1. [독립 함수] list_documents</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/documents.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/documents.py:27`
> > > > > > > - **역할·로직:** HTTP 요청의 값을 서비스에 전달해 문서 목록을 필터 조건으로 조회합니다.
> > > > > > > - **데코레이터:** `router.get('', response_model=list[DocumentOut])`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `dept_id` | `str \| None` | `None` | `위치/키워드` | 부서 식별자 또는 필터 |
> > > > > > > | `security_level` | `str \| None` | `None` | `위치/키워드` | 문서 보안 등급 또는 필터 |
> > > > > > > | `status` | `str \| None` | `None` | `위치/키워드` | 문서 상태 필터 또는 테스트의 기대 HTTP 상태 코드 |
> > > > > > > | `q` | `str \| None` | `None` | `위치/키워드` | 문서 제목·ID 검색어 |
> > > > > > > | `limit` | `Annotated[int, Query(ge=1, le=100)]` | `20` | `위치/키워드` | 최대 조회 건수 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `list[dict]`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return document_service.list_documents(dept_id=dept_id, security_level=security_level, status=status, q=q, limit=limit)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def list_documents(
> > > > > > > >     dept_id: str | None = None, 
> > > > > > > >     security_level: str | None = None,
> > > > > > > >     status: str | None = None, 
> > > > > > > >     q: str | None = None,
> > > > > > > >     limit: Annotated[int, Query(ge=1, le=100)] = 20 
> > > > > > > > ) -> list[dict]:
> > > > > > > >
> > > > > > > >     # 서비스 함수와 연결 (service -> repository -> DB 데이터 조회) 
> > > > > > > >     return document_service.list_documents(
> > > > > > > >         dept_id=dept_id,
> > > > > > > >         security_level=security_level,
> > > > > > > >         status=status,
> > > > > > > >         q=q,
> > > > > > > >         limit=limit
> > > > > > > >     )
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2. [독립 함수] upload_document</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/documents.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/documents.py:46`
> > > > > > > - **역할·로직:** 업로드 파일 확장자를 확인하고 파일을 저장한 뒤 문서 생성 서비스에 정보를 전달합니다.
> > > > > > > - **데코레이터:** `router.post('', response_model=DocumentCreateOut, status_code=201)`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `doc_id` | `Annotated[str, Form()]` | `필수` | `위치/키워드` | 문서 식별자 |
> > > > > > > | `title` | `Annotated[str, Form()]` | `필수` | `위치/키워드` | 제목 |
> > > > > > > | `dept_id` | `Annotated[str, Form()]` | `필수` | `위치/키워드` | 부서 식별자 또는 필터 |
> > > > > > > | `security_level` | `Annotated[str, Form()]` | `필수` | `위치/키워드` | 문서 보안 등급 또는 필터 |
> > > > > > > | `version` | `Annotated[str, Form()]` | `필수` | `위치/키워드` | 문서 버전 문자열 또는 ORM 객체(타입 참고) |
> > > > > > > | `effective_from` | `Annotated[date, Form()]` | `필수` | `위치/키워드` | 문서 시행일 |
> > > > > > > | `file` | `Annotated[UploadFile, File()]` | `필수` | `위치/키워드` | 업로드된 파일 객체 |
> > > > > > > | `logger` | `LoggerDep` | `필수` | `위치/키워드` | 의존성으로 전달받는 로거 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `dict`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return document_service.create_document(doc_id=doc_id, title=title, dept_id=dept_id, security_level=security_level, version=version, effective_from=effective_from, file_path=dest.as_posix(), file_format=ext.lstrip('.'))
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def upload_document(
> > > > > > > >     doc_id: Annotated[str, Form()],
> > > > > > > >     title: Annotated[str, Form()],
> > > > > > > >     dept_id: Annotated[str, Form()],
> > > > > > > >     security_level: Annotated[str, Form()],
> > > > > > > >     version: Annotated[str, Form()],
> > > > > > > >     effective_from: Annotated[date, Form()],
> > > > > > > >     file: Annotated[UploadFile, File()],
> > > > > > > >     logger: LoggerDep,
> > > > > > > > ) -> dict:
> > > > > > > >     safe_name = Path(file.filename or "").name
> > > > > > > >     ext = Path(safe_name).suffix.lower()
> > > > > > > >
> > > > > > > >     if ext not in ALLOWED_EXTS:
> > > > > > > >         
> > > > > > > >         raise ValidationFailed(
> > > > > > > >             f"{ext or '확장자 없는'} 파일은 등록할 수 없습니다. "
> > > > > > > >             "DOCX 또는 PDF 로 변환해 다시 올려 주세요."
> > > > > > > >         )
> > > > > > > >     
> > > > > > > >     UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
> > > > > > > >     dest = UPLOAD_DIR / f"{doc_id}_{version}{ext}"
> > > > > > > >     
> > > > > > > >     with dest.open("wb") as out:
> > > > > > > >         shutil.copyfileobj(file.file, out)
> > > > > > > >
> > > > > > > >     logger.info("문서 파일 저장: %s (%s)", dest, security_level)
> > > > > > > >     
> > > > > > > >     return document_service.create_document(
> > > > > > > >         doc_id=doc_id,
> > > > > > > >         title=title,
> > > > > > > >         dept_id=dept_id,
> > > > > > > >         security_level=security_level,
> > > > > > > >         version=version,
> > > > > > > >         effective_from=effective_from,
> > > > > > > >         file_path=dest.as_posix(),
> > > > > > > >         file_format=ext.lstrip("."),
> > > > > > > >     )
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>3. [독립 함수] get_document</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/api/v1/documents.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/api/v1/documents.py:87`
> > > > > > > - **역할·로직:** HTTP 요청의 값을 서비스에 전달해 문서 한 건을 조회합니다.
> > > > > > > - **데코레이터:** `router.get('/{doc_id}', response_model=DocumentOut)`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `doc_id` | `str` | `필수` | `위치/키워드` | 문서 식별자 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `dict`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return document_service.get_document(doc_id=doc_id)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def get_document(doc_id: str) -> dict:
> > > > > > > >     return document_service.get_document(doc_id=doc_id)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastAPI가 해당 HTTP 요청을 받으면 등록된 핸들러를 호출합니다. 경로는 아래 데코레이터와 FastApi/backend/app/main.py의 /api/v1 라우터 등록을 함께 봅니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/core</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/config.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `Settings`
> > > > > - 파일 수준 함수: `get_settings`, `mask`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] Settings</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/config.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/config.py:5`
> > > > > > - **역할·로직:** 환경변수와 .env 및 기본값을 합쳐 애플리케이션 설정을 제공합니다.
> > > > > > - **상속:** `BaseSettings`
> > > > > > - **클래스 호출 결과:** `Settings` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `is_live`
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore', case_sensitive=False)
> > > > > > app_mode: str = Field(default='mock', pattern='^(mock|live)$')
> > > > > > anthropic_api_key: SecretStr | None = None
> > > > > > llm_model: str = 'claude-haiku-4-5'
> > > > > > max_tokens: int = Field(default=400, ge=1, le=8192)
> > > > > > temperature: float = Field(default=0.0, ge=0.0, le=1.0)
> > > > > > daily_call_limit: int = Field(default=200, ge=1)
> > > > > > max_input_chars: int = Field(default=200, ge=1)
> > > > > > database_url: str = 'sqlite:///./app.db'
> > > > > > debug: bool = False
> > > > > > allow_external_send: bool = False
> > > > > > langfuse_enabled: bool = False
> > > > > > langfuse_host: str = 'http://localhost:3000'
> > > > > > langfuse_public_key: str | None = None
> > > > > > langfuse_secret_key: SecretStr | None = None
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/deps.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/deps.py:15` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/config.py:36` — `Settings.is_live` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/config.py:40` — `get_settings` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/config.py:41` — `get_settings` / 직접 호출
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 1.1 `Settings.is_live`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1.1. [속성 메서드] Settings.is_live</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/core/config.py`
> > > > > > >
> > > > > > > **소속 클래스:** `Settings`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/core/config.py:35`
> > > > > > > - **역할·로직:** 설정의 app_mode가 live인지 판단합니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `bool`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return self.app_mode == 'live'
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def is_live(self) -> bool:
> > > > > > > >         return self.app_mode == "live"
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.is_live처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/integrations/factory.py:20` — `get_llm` / 대상 확인 필요: settings.is_live
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] get_settings</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/config.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/config.py:40`
> > > > > > - **역할·로직:** 환경 설정 객체를 만들어 캐시하고 다음 호출에서 재사용합니다.
> > > > > > - **데코레이터:** `lru_cache`
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Settings`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return Settings()
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_settings() -> Settings:
> > > > > > >     return Settings()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/deps.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/deps.py:16` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/guards.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/core/guards.py:16` — `check_question` / 직접 호출
> > > > > > - `FastApi/backend/app/core/guards.py:37` — `check_daily_limit` / 직접 호출
> > > > > > - `FastApi/backend/app/db/migrations/env.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/migrations/env.py:15` — `모듈 실행부` / 직접 호출
> > > > > > - `FastApi/backend/app/db/session.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/session.py:19` — `get_engine` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/factory.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/factory.py:19` — `get_llm` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:20` — `get_client` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:48` — `ClaudeLLM.__init__` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:65` — `ClaudeLLM._call` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:11` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:95` — `ask` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_core_config.py:1` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_core_config.py:4` — `test_get_settings_returns_same_instance` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_core_config.py:7` — `test_settings_has_defaults` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:16` — `test_check_question_rejects_too_long` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:23` — `test_check_model_rejects_unknown_model` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:26` — `test_check_daily_limit_raises_when_exhausted` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] mask</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/config.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/config.py:44`
> > > > > > - **역할·로직:** 비밀값의 앞부분과 전체 길이만 표시합니다. 값이 없으면 (없음)을 반환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `secret` | `str \| None` | `필수` | `위치/키워드` | 일부만 표시할 비밀 문자열 |
> > > > > > | `keep` | `int` | `8` | `위치/키워드` | 앞에서 남길 글자 수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return '(없음)'
> > > > > > return f'{secret[:keep]}...({len(secret)}자)'
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def mask(secret: str | None, keep: int = 8) -> str:
> > > > > > >     if not secret:
> > > > > > >         return "(없음)"
> > > > > > >     return f"{secret[:keep]}...({len(secret)}자)"
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/exceptions.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `AgentError`, `NotFound`, `PermissionDenied`, `ValidationFailed`, `GuardTripped`, `RateLimited`, `ApprovalRequired`, `ModeNotAvailable`, `ExternalServiceError`, `AuthFailed`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] AgentError</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:2`
> > > > > > - **역할·로직:** HTTP 상태 코드·오류 코드와 메시지·상세정보를 가지는 프로젝트 예외의 부모입니다.
> > > > > > - **상속:** `Exception`
> > > > > > - **클래스 호출 결과:** `AgentError` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `__init__`
> > > > > > - **생성 매개변수:** 아래 `AgentError.__init__`의 self를 제외한 매개변수.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 400
> > > > > > code = 'agent_error'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/core/exceptions.py:8` — `AgentError.__init__` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:9` — `AgentError.__init__` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:12` — `NotFound` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:17` — `PermissionDenied` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:22` — `ValidationFailed` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:27` — `GuardTripped` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:32` — `RateLimited` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:37` — `ApprovalRequired` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:42` — `ModeNotAvailable` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:48` — `ExternalServiceError` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/core/exceptions.py:54` — `AuthFailed` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/main.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/main.py:51` — `handle_agent_error` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/main.py:54` — `handle_agent_error` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:30` — `test_every_domain_exception_is_agent_error` / 참조·타입·콜백 등
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 1.1 `AgentError.__init__`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1.1. [초기화 메서드] AgentError.__init__</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > > >
> > > > > > > **소속 클래스:** `AgentError`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:6`
> > > > > > > - **역할·로직:** 부모 예외를 초기화하고 message와 detail을 객체에 저장합니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > > | `message` | `str` | `필수` | `위치/키워드` | 로그 또는 예외 메시지 |
> > > > > > > | `detail` | `str \| None` | `None` | `키워드 전용` | 추가 오류 상세정보 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `타입 표기 없음`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def __init__(self, message: str, *, detail: str | None = None):
> > > > > > > >         super().__init__(message)  # print(e) -> 메세지 나옴 
> > > > > > > >         self.message = message 
> > > > > > > >         self.detail = detail
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - 이 클래스의 객체 생성 시 자동 호출됩니다. 호출·사용 위치는 위 클래스 항목에도 나열합니다. self는 파이썬이 자동 전달합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/core/exceptions.py:7` — `AgentError.__init__` / 대상 확인 필요: super().__init__
> > > > > > > - `FastApi/backend/app/core/exceptions.py:59` — `AuthFailed.__int__` / 대상 확인 필요: super().__init__
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] NotFound</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:12`
> > > > > > - **역할·로직:** 대상을 찾지 못한 오류(404)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `NotFound` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 404
> > > > > > code = 'not_found'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:12` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:151` — `get_run` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/document_service.py:58` — `get_document` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:61` — `get_document` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:10` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_exceptions.py:34` — `test_detail_is_optional_and_kept` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:38` — `test_detail_is_optional_and_kept` / 직접 호출
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [클래스] PermissionDenied</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:17`
> > > > > > - **역할·로직:** 권한 부족 오류(403)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `PermissionDenied` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 403
> > > > > > code = 'permission_denied'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:11` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [클래스] ValidationFailed</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:22`
> > > > > > - **역할·로직:** 업무 입력 검증 오류(422)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `ValidationFailed` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 422
> > > > > > code = 'validation_failed'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/documents.py:61` — `upload_document` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/document_service.py:92` — `create_document` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:12` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>5. [클래스] GuardTripped</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:27`
> > > > > > - **역할·로직:** 입력 가드 차단 오류(400)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `GuardTripped` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 400
> > > > > > code = 'guard_tripped'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/core/guards.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/core/guards.py:19` — `check_question` / 직접 호출
> > > > > > - `FastApi/backend/app/core/guards.py:21` — `check_question` / 직접 호출
> > > > > > - `FastApi/backend/app/core/guards.py:31` — `check_model` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:85` — `test_golden` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:13` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_guards.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:12` — `test_check_question_rejects_blank` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_guards.py:17` — `test_check_question_rejects_too_long` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_guards.py:21` — `test_check_model_rejects_unknown_model` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>6. [클래스] RateLimited</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:32`
> > > > > > - **역할·로직:** 호출 한도 초과 오류(429)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `RateLimited` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 429
> > > > > > code = 'rate_limited'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/core/guards.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/core/guards.py:39` — `check_daily_limit` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:14` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_guards.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:28` — `test_check_daily_limit_raises_when_exhausted` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>7. [클래스] ApprovalRequired</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:37`
> > > > > > - **역할·로직:** 승인이 필요한 오류(409)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `ApprovalRequired` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 409
> > > > > > code = 'approval_required'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:17` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>8. [클래스] ModeNotAvailable</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:42`
> > > > > > - **역할·로직:** 지원하지 않는 모드 오류(409)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `ModeNotAvailable` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 409
> > > > > > code = 'mode_not_available'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/factory.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/factory.py:21` — `get_llm` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:16` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>9. [클래스] ExternalServiceError</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:48`
> > > > > > - **역할·로직:** 외부 서비스 오류(502)입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `ExternalServiceError` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 502
> > > > > > code = 'external_service_error'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:46` — `ClaudeLLM.__init__` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:51` — `ClaudeLLM.__init__` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:72` — `ClaudeLLM._call` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_exceptions.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_exceptions.py:15` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>10. [클래스] AuthFailed</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:54`
> > > > > > - **역할·로직:** 인증 실패 오류(401)입니다. 현재 초기화 의도로 보이는 메서드 이름이 __int__입니다.
> > > > > > - **상속:** `AgentError`
> > > > > > - **클래스 호출 결과:** `AuthFailed` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `__int__`
> > > > > > - **생성 매개변수:** FastApi/backend/app/core/exceptions.py의 AgentError.__init__(message: str, *, detail: str | None = None)을 상속합니다. message는 필수입니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status_code = 401
> > > > > > code = 'auth_failed'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/auth.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/auth.py:26` — `me` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:3` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/auth_service.py:27` — `authenticate` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:36` — `get_me` / 직접 호출
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 10.1 `AuthFailed.__int__`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>10.1. [인스턴스 메서드] AuthFailed.__int__</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/core/exceptions.py`
> > > > > > >
> > > > > > > **소속 클래스:** `AuthFailed`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/core/exceptions.py:58`
> > > > > > > - **역할·로직:** 부모 예외 초기화를 호출합니다. 이름이 __init__이 아니므로 AuthFailed() 생성 시 자동 실행되지 않습니다. int 변환용 이름인데 정수를 반환하지도 않습니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > > | `message` | `str` | `'사번 또는 비밀번호가 올바르지 않습니다.'` | `위치/키워드` | 로그 또는 예외 메시지 |
> > > > > > > | `detail` | `str \| None` | `None` | `키워드 전용` | 추가 오류 상세정보 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `타입 표기 없음`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def __int__(self, message:str = "사번 또는 비밀번호가 올바르지 않습니다.", *, detail: str | None = None):
> > > > > > > >         super().__init__(message, detail=detail)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/guards.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `check_question`, `check_model`, `check_daily_limit`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] check_question</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/guards.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/guards.py:14`
> > > > > > - **역할·로직:** 질문 앞뒤 공백을 지우고 최소·최대 길이를 검사합니다. 실패하면 GuardTripped입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return q
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def check_question(text: str) -> str:
> > > > > > >     # text : 사용자가 보낸 질문 원문 
> > > > > > >     settings = get_settings() 
> > > > > > >     q = (text or "").strip()      # 값 체크 및 앞뒤 공백 없애기 
> > > > > > >     if len(q) < MIN_QUESTION_LEN:
> > > > > > >         raise GuardTripped("질문이 비어 있거나 너무 짧습니다.")
> > > > > > >     if len(q) > settings.max_input_chars:
> > > > > > >         raise GuardTripped(
> > > > > > >             f"질문이 너무 깁니다 ({len(q)}자)."
> > > > > > >             f"{settings.max_input_chars}자 이낼로 줄여주세요."
> > > > > > >         )
> > > > > > >     return q
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:75` — `ask` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:9` — `test_check_question_passed_and_strips` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:13` — `test_check_question_rejects_blank` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:18` — `test_check_question_rejects_too_long` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] check_model</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/guards.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/guards.py:28`
> > > > > > - **역할·로직:** 모델 이름이 허용 목록에 있는지 검사합니다. 실패하면 GuardTripped입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `model` | `str` | `필수` | `위치/키워드` | 검사할 모델 이름 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return model
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def check_model(model: str) -> str:
> > > > > > >     # model : 부르려는 모델 이름 
> > > > > > >     if model not in ALLOWED_MODELS:
> > > > > > >         raise GuardTripped(f"허용되지 않은 모델입니다: {model}")
> > > > > > >     return model
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:87` — `test_golden` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:22` — `test_check_model_rejects_unknown_model` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:23` — `test_check_model_rejects_unknown_model` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] check_daily_limit</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/guards.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/guards.py:35`
> > > > > > - **역할·로직:** 이미 사용한 호출 수가 일일 한도 이상인지 검사합니다. 이상이면 RateLimited입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `used_today` | `int` | `필수` | `위치/키워드` | 오늘 이미 사용한 호출 수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def check_daily_limit(used_today: int) -> None:
> > > > > > >     # used_today: 오늘 이미 사용한 호출 수 
> > > > > > >     settings = get_settings() 
> > > > > > >     if used_today >= settings.daily_call_limit: 
> > > > > > >         raise RateLimited(
> > > > > > >             f"오늘 호출 한도({settings.daily_call_limit}회)를 모두 사용했습니다."
> > > > > > >         )
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/tests/test_guards.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_guards.py:27` — `test_check_daily_limit_raises_when_exhausted` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_guards.py:29` — `test_check_daily_limit_raises_when_exhausted` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/logging.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `setup_logging`, `get_logger`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] setup_logging</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/logging.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/logging.py:14`
> > > > > > - **역할·로직:** 로그 핸들러와 출력 형식·수준을 설정합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `level` | `int` | `logging.INFO` | `위치/키워드` | 로그 수준 |
> > > > > > | `stream` | `타입 표기 없음` | `None` | `위치/키워드` | 로그 출력 스트림 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def setup_logging(level: int = logging.INFO, stream=None) -> None:
> > > > > > >
> > > > > > >     # global : 함수안에서 모듈의 전역변수 수정 가능하게 해주는 명령어 
> > > > > > >     global _CONFIGURED
> > > > > > >     if _CONFIGURED:  # 설정을 이미 했으면 메서드 강제 종료 
> > > > > > >         return 
> > > > > > >
> > > > > > >     # 핸들러 : 로그를 어디로 내보낼지 설정 
> > > > > > >     handler = logging.StreamHandler(stream or sys.stdout)
> > > > > > >     # 포매터 : 로그 한줄의 모양 설정 
> > > > > > >     handler.setFormatter(logging.Formatter(_FORMAT, datefmt=_DATEFMT))
> > > > > > >
> > > > > > >     root = logging.getLogger() # 이름 없는 최상위 로거 
> > > > > > >     root.setLevel(level)
> > > > > > >     root.handlers = [handler]  # 기존 핸들러 밀어내고 하나만 놓기
> > > > > > >     # 터미널 출력과 파일 출력을 동시에 할려면 각각의 핸들러를 만들어서 둘다 넣기
> > > > > > >
> > > > > > >     for name in _NOISY:
> > > > > > >         logging.getLogger(name).setLevel(logging.WARNING)
> > > > > > >
> > > > > > >     _CONFIGURED = True
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/core/logging.py:40` — `get_logger` / 직접 호출
> > > > > > - `FastApi/backend/app/main.py:12` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/main.py:18` — `lifespan` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] get_logger</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/logging.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/logging.py:39`
> > > > > > - **역할·로직:** 주어진 이름의 로거를 가져옵니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `logging.Logger`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return logging.getLogger(name)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_logger(name: str) -> logging.Logger:
> > > > > > >     setup_logging()
> > > > > > >     return logging.getLogger(name)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/deps.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/deps.py:28` — `get_request_logger` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:8` — `모듈 실행부` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:11` — `모듈 실행부` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:19` — `모듈 실행부` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/core/security.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `hash_password`, `verify_password`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] hash_password</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/security.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/security.py:6`
> > > > > > - **역할·로직:** 평문 비밀번호를 저장용 해시로 변환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `raw` | `str` | `필수` | `위치/키워드` | 평문 비밀번호 또는 HTML 원문 허용 여부(타입 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return bcrypt.hashpw(raw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def hash_password(raw: str) -> str:
> > > > > > >     return bcrypt.hashpw(raw.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:37` — `_seed` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] verify_password</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/core/security.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/core/security.py:10`
> > > > > > - **역할·로직:** 평문 비밀번호와 저장된 해시가 일치하는지 검사합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `raw` | `str` | `필수` | `위치/키워드` | 평문 비밀번호 또는 HTML 원문 허용 여부(타입 참고) |
> > > > > > | `hashed` | `str` | `필수` | `위치/키워드` | 저장된 비밀번호 해시 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `bool`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return bcrypt.checkpw(raw.encode('utf-8'), hashed.encode('utf-8'))
> > > > > > return False
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def verify_password(raw: str, hashed: str) -> bool:
> > > > > > >     try:
> > > > > > >         return bcrypt.checkpw(raw.encode("utf-8"), hashed.encode("utf-8"))
> > > > > > >     except (ValueError, TypeError):
> > > > > > >         return False
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/auth_service.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/auth_service.py:26` — `authenticate` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/db</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/db/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/db/init_db.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `init_db`, `main`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] init_db</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/init_db.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/init_db.py:5`
> > > > > > - **역할·로직:** 모델 메타데이터의 create_all로 없는 테이블을 생성합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `engine` | `Engine \| None` | `None` | `위치/키워드` | DB 엔진; 생략 시 기본 연결 사용 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def init_db(engine: Engine | None = None) -> None:
> > > > > > >
> > > > > > >     from app.models import Base
> > > > > > >     Base.metadata.create_all(engine or get_engine())
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/init_db.py:12` — `main` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] main</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/init_db.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/init_db.py:11`
> > > > > > - **역할·로직:** DB 테이블 생성과 초기 데이터 준비를 실행하는 진입 함수입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def main() -> None:
> > > > > > >     init_db()
> > > > > > >     print("테이블 생성 완료")
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/init_db.py:16` — `모듈 실행부` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/db/seed.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `count_rows`, `seed_all`, `_seed`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] count_rows</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/seed.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/seed.py:12`
> > > > > > - **역할·로직:** 부서·사용자·문서·버전 테이블의 행 수를 조회합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict[str, int]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {'departments': session.scalar(select(func.count()).select_from(Department)) or 0, 'users': session.scalar(select(func.count()).select_from(User)) or 0, 'documents': session.scalar(select(func.count()).select_from(Document)) or 0, 'versions': session.scalar(select(func.count()).select_from(DocumentVersion)) or 0}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def count_rows(session: Session) -> dict[str, int]:
> > > > > > >
> > > > > > >     return {
> > > > > > >         "departments": session.scalar(select(func.count()).select_from(Department)) or 0,
> > > > > > >         "users": session.scalar(select(func.count()).select_from(User)) or 0,
> > > > > > >         "documents": session.scalar(select(func.count()).select_from(Document)) or 0,
> > > > > > >         "versions": session.scalar(select(func.count()).select_from(DocumentVersion)) or 0,
> > > > > > >     }
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:32` — `_seed` / 직접 호출
> > > > > > - `FastApi/backend/app/db/seed.py:51` — `_seed` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] seed_all</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/seed.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/seed.py:22`
> > > > > > - **역할·로직:** 전달된 세션을 사용하거나 자체 세션을 열어 초기 데이터를 넣습니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session \| None` | `None` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict[str, int]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _seed(session)
> > > > > > return _seed(s)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def seed_all(session: Session | None = None) -> dict[str, int]:
> > > > > > >     if session is not None:
> > > > > > >         return _seed(session)
> > > > > > >     with session_scope() as s:
> > > > > > >         return _seed(s)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] _seed</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/seed.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/seed.py:29`
> > > > > > - **역할·로직:** 이미 문서가 있으면 건수만 반환합니다. 없으면 부서·사용자·문서·버전 데이터를 추가하고 건수를 반환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict[str, int]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return count_rows(session)
> > > > > > return count_rows(session)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _seed(session: Session) -> dict[str, int]:
> > > > > > >
> > > > > > >     if session.scalar(select(func.count()).select_from(Document)):
> > > > > > >         return count_rows(session)
> > > > > > >
> > > > > > >     session.add_all(Department(**row) for row in DEPARTMENTS)
> > > > > > >
> > > > > > >
> > > > > > >     temp_hash = hash_password(TEMP_PASSWORD)
> > > > > > >     session.add_all(User(**row, password_hash=temp_hash) for row in USERS)
> > > > > > >     session.flush()   
> > > > > > >
> > > > > > >     for doc in DOCUMENTS:
> > > > > > >         
> > > > > > >         fields = {k: v for k, v in doc.items() if k != "versions"}
> > > > > > >         session.add(Document(**fields))
> > > > > > >         session.flush()
> > > > > > >         session.add_all(
> > > > > > >             DocumentVersion(doc_id=doc["id"], **ver) for ver in doc["versions"]
> > > > > > >         )
> > > > > > >     session.flush()
> > > > > > >
> > > > > > >     return count_rows(session)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:24` — `seed_all` / 직접 호출
> > > > > > - `FastApi/backend/app/db/seed.py:26` — `seed_all` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/db/seed_data.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 부서·사용자·문서 시드 상수입니다. FastApi/backend/app/db/seed.py의 _seed에서 읽습니다. 비밀번호 등 상수의 실제 값은 싣지 않습니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/db/session.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `get_engine`, `get_sessionmaker`, `session_scope`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] get_engine</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/session.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/session.py:16`
> > > > > > - **역할·로직:** URL에 대응하는 SQLAlchemy 엔진을 캐시에서 가져오거나 새로 만듭니다. SQLite이면 전용 연결 설정을 추가합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `url` | `str \| None` | `None` | `위치/키워드` | DB 연결 URL; 생략 시 설정 사용 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Engine`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _ENGINES[resolved]
> > > > > > return engine
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_engine(url: str | None = None) -> Engine:
> > > > > > >
> > > > > > >     # 이미 만들어진 엔진이라면 만들어진 것 리턴하며 종료 처리 
> > > > > > >     resolved = url or get_settings().database_url # 환경변수에서 DB URL 가져와 적용 
> > > > > > >     if resolved in _ENGINES:       
> > > > > > >         return _ENGINES[resolved]  
> > > > > > >
> > > > > > >     # SQLite 설정 추가 
> > > > > > >     connect_args: dict[str, object] = {}
> > > > > > >     is_sqlite = resolved.startswith("sqlite")
> > > > > > >     if is_sqlite:
> > > > > > >         connect_args["check_same_thread"] = False
> > > > > > >
> > > > > > >     # 엔진 생성 
> > > > > > >     engine = create_engine(resolved, connect_args=connect_args)
> > > > > > >
> > > > > > >     # SQLite 설정 추가 
> > > > > > >     if is_sqlite:        
> > > > > > >         @event.listens_for(engine, "connect")
> > > > > > >         def _enable_sqlite_foreign_keys(dbapi_connection, connection_record) -> None: 
> > > > > > >             cursor = dbapi_connection.cursor()
> > > > > > >             cursor.execute("PRAGMA foreign_keys=ON")
> > > > > > >             cursor.close()
> > > > > > >
> > > > > > >     # 새로 만들어진 엔진 저장하며 리턴 
> > > > > > >     _ENGINES[resolved] = engine
> > > > > > >     return engine
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/init_db.py:3` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/init_db.py:8` — `init_db` / 직접 호출
> > > > > > - `FastApi/backend/app/db/session.py:46` — `get_sessionmaker` / 직접 호출
> > > > > >
> > > > > > **이 함수 안의 함수**
> > > > > >
> > > > > > - 1.1 `get_engine._enable_sqlite_foreign_keys`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1.1. [중첩 함수] get_engine._enable_sqlite_foreign_keys</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/db/session.py`
> > > > > > >
> > > > > > > **소속 함수:** `get_engine`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/db/session.py:35`
> > > > > > > - **역할·로직:** SQLite 연결에서 PRAGMA foreign_keys=ON을 실행합니다.
> > > > > > > - **데코레이터:** `event.listens_for(engine, 'connect')`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `dbapi_connection` | `타입 표기 없음` | `필수` | `위치/키워드` | 이벤트에서 받은 실제 DBAPI 연결 |
> > > > > > > | `connection_record` | `타입 표기 없음` | `필수` | `위치/키워드` | SQLAlchemy 연결 풀의 연결 기록 |
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `None`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def _enable_sqlite_foreign_keys(dbapi_connection, connection_record) -> None: 
> > > > > > > >             cursor = dbapi_connection.cursor()
> > > > > > > >             cursor.execute("PRAGMA foreign_keys=ON")
> > > > > > > >             cursor.close()
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastApi/backend/app/db/session.py의 get_engine 안에서 SQLAlchemy connect 이벤트에 등록됩니다. SQLite DB 연결 시 호출됩니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] get_sessionmaker</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/session.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/session.py:45`
> > > > > > - **역할·로직:** 지정 엔진 또는 기본 엔진에 연결된 세션 생성기를 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `engine` | `Engine \| None` | `None` | `위치/키워드` | DB 엔진; 생략 시 기본 연결 사용 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `sessionmaker[Session]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return sessionmaker(bind=engine or get_engine(), expire_on_commit=False)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_sessionmaker(engine: Engine | None = None) -> sessionmaker[Session]:
> > > > > > >     return sessionmaker(bind=engine or get_engine(), expire_on_commit=False)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/deps.py:11` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/deps.py:34` — `get_db` / 직접 호출
> > > > > > - `FastApi/backend/app/db/session.py:52` — `session_scope` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] session_scope</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/db/session.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/db/session.py:51`
> > > > > > - **역할·로직:** 세션을 제공하고 정상 종료 시 commit, 오류 시 rollback, 마지막에 close를 수행합니다.
> > > > > > - **데코레이터:** `contextmanager`
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Iterator[Session]`
> > > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > > - 호출하면 컨텍스트 매니저를 반환합니다. with/async with 진입 시 아래 값을 제공하고, 블록 종료 시 yield 뒤 정리 코드를 실행합니다.
> > > > > > - 제공 값: `(yield session)`
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def session_scope() -> Iterator[Session]:
> > > > > > >     session = get_sessionmaker()()
> > > > > > >     try:
> > > > > > >         yield session
> > > > > > >         session.commit()
> > > > > > >     except Exception:
> > > > > > >         session.rollback()
> > > > > > >         raise
> > > > > > >     finally:
> > > > > > >         session.close()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:25` — `seed_all` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/auth_service.py:22` — `authenticate` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:32` — `get_me` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:13` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:59` — `_record_usage` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:86` — `ask` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:137` — `ask` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:148` — `get_run` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/document_service.py:40` — `list_documents` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:55` — `get_document` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:78` — `create_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[폴더] FastApi/backend/app/db/migrations</h1></summary>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/README</h1></summary>
> > > > > >
> > > > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > > > - **사용 위치:** 마이그레이션 안내 문서입니다. 실행 함수가 아닙니다.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/env.py</h1></summary>
> > > > > >
> > > > > > **파일 구성**
> > > > > >
> > > > > > - 클래스: 없음
> > > > > > - 파일 수준 함수: `run_migrations_offline`, `run_migrations_online`
> > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > >
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1. [독립 함수] run_migrations_offline</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/env.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/env.py:36`
> > > > > > > - **역할·로직:** DB 연결 없이 SQL을 생성하는 방식으로 Alembic 마이그레이션을 구성합니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > 없음.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `None`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def run_migrations_offline() -> None:
> > > > > > > >     """Run migrations in 'offline' mode.
> > > > > > > >
> > > > > > > >     This configures the context with just a URL
> > > > > > > >     and not an Engine, though an Engine is acceptable
> > > > > > > >     here as well.  By skipping the Engine creation
> > > > > > > >     we don't even need a DBAPI to be available.
> > > > > > > >
> > > > > > > >     Calls to context.execute() here emit the given string to the
> > > > > > > >     script output.
> > > > > > > >
> > > > > > > >     """
> > > > > > > >     url = config.get_main_option("sqlalchemy.url")
> > > > > > > >     context.configure(
> > > > > > > >         url=url,
> > > > > > > >         target_metadata=target_metadata,
> > > > > > > >         literal_binds=True,
> > > > > > > >         dialect_opts={"paramstyle": "named"},
> > > > > > > >     )
> > > > > > > >
> > > > > > > >     with context.begin_transaction():
> > > > > > > >         context.run_migrations()
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/db/migrations/env.py:83` — `모듈 실행부` / 직접 호출
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2. [독립 함수] run_migrations_online</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/env.py`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/env.py:60`
> > > > > > > - **역할·로직:** DB 연결을 열고 트랜잭션 안에서 Alembic 마이그레이션을 실행합니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > 없음.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `None`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def run_migrations_online() -> None:
> > > > > > > >     """Run migrations in 'online' mode.
> > > > > > > >
> > > > > > > >     In this scenario we need to create an Engine
> > > > > > > >     and associate a connection with the context.
> > > > > > > >
> > > > > > > >     """
> > > > > > > >     connectable = engine_from_config(
> > > > > > > >         config.get_section(config.config_ini_section, {}),
> > > > > > > >         prefix="sqlalchemy.",
> > > > > > > >         poolclass=pool.NullPool,
> > > > > > > >     )
> > > > > > > >
> > > > > > > >     with connectable.connect() as connection:
> > > > > > > >         context.configure(
> > > > > > > >             connection=connection, target_metadata=target_metadata
> > > > > > > >         )
> > > > > > > >
> > > > > > > >         with context.begin_transaction():
> > > > > > > >             context.run_migrations()
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/db/migrations/env.py:85` — `모듈 실행부` / 직접 호출
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/script.py.mako</h1></summary>
> > > > > >
> > > > > > - **함수·클래스:** Alembic 파일 생성 템플릿입니다. upgrade() -> None, downgrade() -> None 형태를 생성하며 매개변수는 없습니다. 동작은 생성 시 삽입되는 스키마 변경 내용입니다.
> > > > > > - **사용 위치:** FastApi/backend/alembic.ini가 지정한 마이그레이션 디렉터리에서 Alembic이 새 revision 생성 시 사용합니다. 생성된 함수는 versions의 각 파일에 별도 나열했습니다.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h1>[폴더] FastApi/backend/app/db/migrations/versions</h1></summary>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py</h1></summary>
> > > > > > >
> > > > > > > **파일 구성**
> > > > > > >
> > > > > > > - 클래스: 없음
> > > > > > > - 파일 수준 함수: `upgrade`, `downgrade`
> > > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > > >
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>1. [독립 함수] upgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py:21`
> > > > > > > > - **역할·로직:** 해당 리비전의 테이블·인덱스 등 스키마 변경을 DB에 적용합니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def upgrade() -> None:
> > > > > > > > >     """Upgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.create_table('usage_logs',
> > > > > > > > >     sa.Column('id', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('run_id', sa.String(length=32), nullable=False),
> > > > > > > > >     sa.Column('model', sa.String(length=64), nullable=False),
> > > > > > > > >     sa.Column('input_tok', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('cache_tok', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('output_tok', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('cost_krw', sa.Float(), nullable=False),
> > > > > > > > >     sa.Column('occurred_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.ForeignKeyConstraint(['run_id'], ['runs.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id')
> > > > > > > > >     )
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>2. [독립 함수] downgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/0f82d3f2c172_add_usage_logs.py:41`
> > > > > > > > - **역할·로직:** 해당 리비전의 스키마 변경을 되돌립니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def downgrade() -> None:
> > > > > > > > >     """Downgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.drop_table('usage_logs')
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py</h1></summary>
> > > > > > >
> > > > > > > **파일 구성**
> > > > > > >
> > > > > > > - 클래스: 없음
> > > > > > > - 파일 수준 함수: `upgrade`, `downgrade`
> > > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > > >
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>1. [독립 함수] upgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py:21`
> > > > > > > > - **역할·로직:** 해당 리비전의 테이블·인덱스 등 스키마 변경을 DB에 적용합니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def upgrade() -> None:
> > > > > > > > >     """Upgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.create_table('runs',
> > > > > > > > >     sa.Column('id', sa.String(length=32), nullable=False),
> > > > > > > > >     sa.Column('user_id', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('question', sa.Text(), nullable=False),
> > > > > > > > >     sa.Column('answer', sa.Text(), nullable=True),
> > > > > > > > >     sa.Column('status', sa.String(length=24), nullable=False),
> > > > > > > > >     sa.Column('latency_ms', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('mode', sa.String(length=8), nullable=False),
> > > > > > > > >     sa.Column('sources', sa.JSON(), nullable=True),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id')
> > > > > > > > >     )
> > > > > > > > >     op.create_table('run_steps',
> > > > > > > > >     sa.Column('id', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('run_id', sa.String(length=32), nullable=False),
> > > > > > > > >     sa.Column('ord', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('name', sa.String(length=64), nullable=False),
> > > > > > > > >     sa.Column('ok', sa.Boolean(), nullable=False),
> > > > > > > > >     sa.Column('ms', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('detail', sa.Text(), nullable=True),
> > > > > > > > >     sa.ForeignKeyConstraint(['run_id'], ['runs.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id')
> > > > > > > > >     )
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>2. [독립 함수] downgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/5b1740bb3da0_add_runs_and_run_steps.py:52`
> > > > > > > > - **역할·로직:** 해당 리비전의 스키마 변경을 되돌립니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def downgrade() -> None:
> > > > > > > > >     """Downgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.drop_table('run_steps')
> > > > > > > > >     op.drop_table('runs')
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h1>[파일] FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py</h1></summary>
> > > > > > >
> > > > > > > **파일 구성**
> > > > > > >
> > > > > > > - 클래스: 없음
> > > > > > > - 파일 수준 함수: `upgrade`, `downgrade`
> > > > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > > > >
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>1. [독립 함수] upgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py:21`
> > > > > > > > - **역할·로직:** 해당 리비전의 테이블·인덱스 등 스키마 변경을 DB에 적용합니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def upgrade() -> None:
> > > > > > > > >     """Upgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.create_table('departments',
> > > > > > > > >     sa.Column('id', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('name', sa.String(length=50), nullable=False),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.PrimaryKeyConstraint('id'),
> > > > > > > > >     sa.UniqueConstraint('name')
> > > > > > > > >     )
> > > > > > > > >     op.create_table('users',
> > > > > > > > >     sa.Column('id', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('emp_no', sa.String(length=16), nullable=False),
> > > > > > > > >     sa.Column('name', sa.String(length=50), nullable=False),
> > > > > > > > >     sa.Column('dept_id', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('role', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('clearance', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('password_hash', sa.String(length=100), nullable=False),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.ForeignKeyConstraint(['dept_id'], ['departments.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id')
> > > > > > > > >     )
> > > > > > > > >     op.create_index(op.f('ix_users_emp_no'), 'users', ['emp_no'], unique=True)
> > > > > > > > >     op.create_table('documents',
> > > > > > > > >     sa.Column('id', sa.String(length=20), nullable=False),
> > > > > > > > >     sa.Column('title', sa.String(length=200), nullable=False),
> > > > > > > > >     sa.Column('dept_id', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('security_level', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('owner_id', sa.Integer(), nullable=True),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.ForeignKeyConstraint(['dept_id'], ['departments.id'], ),
> > > > > > > > >     sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id')
> > > > > > > > >     )
> > > > > > > > >     op.create_index(op.f('ix_documents_dept_id'), 'documents', ['dept_id'], unique=False)
> > > > > > > > >     op.create_index(op.f('ix_documents_security_level'), 'documents', ['security_level'], unique=False)
> > > > > > > > >     op.create_table('document_versions',
> > > > > > > > >     sa.Column('id', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('doc_id', sa.String(length=20), nullable=False),
> > > > > > > > >     sa.Column('version', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('status', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('effective_from', sa.Date(), nullable=False),
> > > > > > > > >     sa.Column('expires_at', sa.Date(), nullable=True),
> > > > > > > > >     sa.Column('file_path', sa.String(length=300), nullable=True),
> > > > > > > > >     sa.Column('file_format', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('chunk_count', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('embed_model', sa.String(length=50), nullable=True),
> > > > > > > > >     sa.Column('index_status', sa.String(length=10), nullable=False),
> > > > > > > > >     sa.Column('index_progress', sa.Integer(), nullable=False),
> > > > > > > > >     sa.Column('indexed_at', sa.Date(), nullable=True),
> > > > > > > > >     sa.Column('created_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.Column('updated_at', sa.DateTime(), nullable=False),
> > > > > > > > >     sa.ForeignKeyConstraint(['doc_id'], ['documents.id'], ),
> > > > > > > > >     sa.PrimaryKeyConstraint('id'),
> > > > > > > > >     sa.UniqueConstraint('doc_id', 'version', name='uq_doc_version')
> > > > > > > > >     )
> > > > > > > > >     op.create_index(op.f('ix_document_versions_doc_id'), 'document_versions', ['doc_id'], unique=False)
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary><h2>2. [독립 함수] downgrade</h2></summary>
> > > > > > > >
> > > > > > > > **소속 파일:** `FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py`
> > > > > > > >
> > > > > > > > - **정의 파일:** `FastApi/backend/app/db/migrations/versions/df6947bee893_initial_schema.py:84`
> > > > > > > > - **역할·로직:** 해당 리비전의 스키마 변경을 되돌립니다.
> > > > > > > >
> > > > > > > > **매개변수**
> > > > > > > >
> > > > > > > > 없음.
> > > > > > > >
> > > > > > > > **반환값**
> > > > > > > >
> > > > > > > > - 선언: `None`
> > > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > > >
> > > > > > > > <details>
> > > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > > >
> > > > > > > > > ```python
> > > > > > > > > def downgrade() -> None:
> > > > > > > > >     """Downgrade schema."""
> > > > > > > > >     # ### commands auto generated by Alembic - please adjust! ###
> > > > > > > > >     op.drop_index(op.f('ix_document_versions_doc_id'), table_name='document_versions')
> > > > > > > > >     op.drop_table('document_versions')
> > > > > > > > >     op.drop_index(op.f('ix_documents_security_level'), table_name='documents')
> > > > > > > > >     op.drop_index(op.f('ix_documents_dept_id'), table_name='documents')
> > > > > > > > >     op.drop_table('documents')
> > > > > > > > >     op.drop_index(op.f('ix_users_emp_no'), table_name='users')
> > > > > > > > >     op.drop_table('users')
> > > > > > > > >     op.drop_table('departments')
> > > > > > > > > ```
> > > > > > > > >
> > > > > > > > </details>
> > > > > > > >
> > > > > > > > **자동 호출·사용 방식**
> > > > > > > >
> > > > > > > > - Alembic이 리비전 체인에 따라 호출합니다. 실행 환경: FastApi/backend/app/db/migrations/env.py, 설정: FastApi/backend/alembic.ini.
> > > > > > > >
> > > > > > > > **호출·사용 위치**
> > > > > > > >
> > > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/integrations</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/integrations/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/integrations/factory.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `_live_llm`, `get_llm`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] _live_llm</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/factory.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/factory.py:12`
> > > > > > - **역할·로직:** ClaudeLLM 객체를 생성하고 캐시해 재사용합니다.
> > > > > > - **데코레이터:** `lru_cache`
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `LLMPort`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return ClaudeLLM()
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _live_llm() -> LLMPort:
> > > > > > >     # live 모드일때만 import해서 ClaudeLLM 생성해주기 
> > > > > > >     from app.integrations.llm_claude import ClaudeLLM
> > > > > > >     return ClaudeLLM()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/factory.py:25` — `get_llm` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] get_llm</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/factory.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/factory.py:18`
> > > > > > - **역할·로직:** live 설정에서는 캐시된 Claude 어댑터를 반환합니다. 다른 모드는 ModeNotAvailable로 거절합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `LLMPort`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _live_llm()
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_llm() -> LLMPort:
> > > > > > >     settings = get_settings()  # 환경 설정 정보 가져오기 
> > > > > > >     if not settings.is_live: # live가 아니다 
> > > > > > >         raise ModeNotAvailable(
> > > > > > >             "테스트용 mock 어댑터는 만들지 않았습니다."
> > > > > > >             ".env의 APP_MODE 를 live로 두고 터미널에서 부르세요."
> > > > > > >         )
> > > > > > >     return _live_llm()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **자동 호출·사용 방식**
> > > > > >
> > > > > > - FastApi/backend/tests/test_chat_golden.py의 test_golden에서 monkeypatch.setattr(factory, "get_llm", lambda: stub)로 임시 교체됩니다. 문자열로 지정하는 교체이므로 일반 이름 참조 목록과 별도로 표시합니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:78` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/integrations/langfuse_client.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `get_client`, `_quiet`, `trace`, `score`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] get_client</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/langfuse_client.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/langfuse_client.py:14`
> > > > > > - **역할·로직:** Langfuse 활성화와 키 설정을 확인하고 클라이언트 생성을 한 번 시도합니다. 비활성화·실패 시 None입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > 없음.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `타입 표기 없음`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _client
> > > > > > return None
> > > > > > return None
> > > > > > return _client
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_client():
> > > > > > >     global _client, _tried
> > > > > > >     if _tried:
> > > > > > >         return _client        
> > > > > > >     _tried = True
> > > > > > >
> > > > > > >     settings = get_settings()
> > > > > > >     if not settings.langfuse_enabled:
> > > > > > >         return None            
> > > > > > >
> > > > > > >     if not settings.langfuse_public_key or settings.langfuse_secret_key is None:
> > > > > > >         log.warning("LANGFUSE_ENABLED=true 인데 키가 비어 있습니다. 관측을 건너뜁니다")
> > > > > > >         return None
> > > > > > >
> > > > > > >     try:
> > > > > > >         from langfuse import Langfuse
> > > > > > >
> > > > > > >         _client = Langfuse(
> > > > > > >             public_key=settings.langfuse_public_key,
> > > > > > >             secret_key=settings.langfuse_secret_key.get_secret_value(),
> > > > > > >             host=settings.langfuse_host,
> > > > > > >         )
> > > > > > >     except Exception as exc:                 
> > > > > > >         log.warning("Langfuse 클라이언트를 만들지 못했습니다 (무시하고 계속): %s", exc)
> > > > > > >         _client = None
> > > > > > >     return _client
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:55` — `trace` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:75` — `score` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] _quiet</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/langfuse_client.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/langfuse_client.py:44`
> > > > > > - **역할·로직:** 첫 관측 오류는 warning, 이후 오류는 debug로 기록합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `message` | `str` | `필수` | `위치/키워드` | 로그 또는 예외 메시지 |
> > > > > > | `exc` | `Exception` | `필수` | `위치/키워드` | 처리할 예외 객체 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _quiet(message: str, exc: Exception) -> None:
> > > > > > >     global _warned
> > > > > > >     if not _warned:
> > > > > > >         _warned = True
> > > > > > >         log.warning("%s (무시하고 계속): %s", message, exc)
> > > > > > >     else:
> > > > > > >         log.debug("%s: %s", message, exc)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:66` — `trace` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/langfuse_client.py:81` — `score` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] trace</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/langfuse_client.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/langfuse_client.py:54`
> > > > > > - **역할·로직:** Langfuse trace 생성을 시도하고 핸들을 with 블록에 제공합니다. 생성 실패 시에도 블록을 실행합니다.
> > > > > > - **데코레이터:** `contextmanager`
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > > | `run_id` | `str` | `필수` | `키워드 전용` | 질문 한 건의 실행 식별자 |
> > > > > > | `user_id` | `str` | `''` | `키워드 전용` | 실행 사용자의 식별자 |
> > > > > > | `metadata` | `dict \| None` | `None` | `키워드 전용` | trace에 붙일 부가정보 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `타입 표기 없음`
> > > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > > - 호출하면 컨텍스트 매니저를 반환합니다. with/async with 진입 시 아래 값을 제공하고, 블록 종료 시 yield 뒤 정리 코드를 실행합니다.
> > > > > > - 제공 값: `(yield handle)`
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def trace(name: str, *, run_id: str, user_id: str = "", metadata: dict | None = None):
> > > > > > >     client = get_client()
> > > > > > >     handle = None
> > > > > > >     if client is not None:
> > > > > > >         try:
> > > > > > >             handle = client.trace(
> > > > > > >                 id=run_id,
> > > > > > >                 name=name,
> > > > > > >                 user_id=user_id,
> > > > > > >                 metadata=metadata or {},
> > > > > > >             )
> > > > > > >         except Exception as exc:              
> > > > > > >             _quiet("Langfuse 트레이스를 시작하지 못했습니다", exc)
> > > > > > >
> > > > > > >     try:
> > > > > > >         yield handle
> > > > > > >     finally:
> > > > > > >         pass
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:81` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:99` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [독립 함수] score</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/langfuse_client.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/langfuse_client.py:74`
> > > > > > - **역할·로직:** 실행 번호에 연결된 점수를 Langfuse에 기록합니다. 기록 실패는 로그를 남기고 넘깁니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `run_id` | `str` | `필수` | `위치/키워드` | 질문 한 건의 실행 식별자 |
> > > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > > | `value` | `float` | `필수` | `위치/키워드` | 변환할 값; call_port에서는 프롬프트 값 객체, score에서는 점수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def score(run_id: str, name: str, value: float) -> None:
> > > > > > >     client = get_client()
> > > > > > >     if client is None:
> > > > > > >         return
> > > > > > >     try:
> > > > > > >         client.score(trace_id=run_id, name=name, value=value)
> > > > > > >     except Exception as exc:                  
> > > > > > >         _quiet("Langfuse 점수를 남기지 못했습니다", exc)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:81` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:135` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/integrations/llm_claude.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `ClaudeLLM`
> > > > > - 파일 수준 함수: `estimate_cost_krw`, `_load_prompt`, `_cotext_block`, `_extract_json`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] estimate_cost_krw</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:16`
> > > > > > - **역할·로직:** 입력·출력 토큰 수에 코드의 단가와 환율을 곱해 추정 원화 비용을 계산합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `input_tok` | `int` | `필수` | `위치/키워드` | 입력 토큰 수 |
> > > > > > | `output_tok` | `int` | `필수` | `위치/키워드` | 출력 토큰 수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `float`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return round(usd * USD_KRW, 1)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def estimate_cost_krw(input_tok: int, output_tok: int) -> float:
> > > > > > >     
> > > > > > >     usd = input_tok / 1000000 * PRICING['input'] + output_tok / 1000000 * PRICING['output']
> > > > > > >     return round(usd * USD_KRW, 1)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:118` — `ClaudeLLM.answer` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] _load_prompt</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:22`
> > > > > > - **역할·로직:** 프롬프트 파일이 있으면 읽고 없으면 빈 문자열을 반환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return path.read_text(encoding='utf-8') if path.exists() else ''
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _load_prompt(name: str) -> str:
> > > > > > >     path = PROMPTS / name
> > > > > > >     return path.read_text(encoding="utf-8") if path.exists() else ""
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:104` — `ClaudeLLM.answer` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] _cotext_block</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:27`
> > > > > > - **역할·로직:** 근거 목록의 제목·버전·위치·유사도·인용문을 모델에게 보낼 한 문자열로 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `contexts` | `list[dict]` | `필수` | `위치/키워드` | 모델에게 전달할 근거 문서 dict 목록 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return '\n\n'.join(lines) if lines else '(근거 문서 없음)'
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _cotext_block(contexts: list[dict]) -> str:
> > > > > > >     # contexts : 근거 항목 목록  
> > > > > > >     lines = []
> > > > > > >     for i, c in enumerate(contexts, 1):
> > > > > > >         lines.append(
> > > > > > >             f"[근거 {i}] {c.get('title')} {c.get('version')} · {c.get('locator')} "
> > > > > > >             f"(유사도 {c.get('score', 0):.2f})\n{c.get('quote') or c.get('text') or ''}"
> > > > > > >         )
> > > > > > >     return "\n\n".join(lines) if lines else "(근거 문서 없음)"
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:107` — `ClaudeLLM.answer` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [클래스] ClaudeLLM</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:38`
> > > > > > - **역할·로직:** LLMPort 규약에 맞춰 Claude SDK를 호출하는 실제 어댑터입니다.
> > > > > > - **상속:** 명시적 부모 없음(object)
> > > > > > - **클래스 호출 결과:** `ClaudeLLM` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `__init__`, `_call`, `answer`
> > > > > > - **생성 매개변수:** 아래 `ClaudeLLM.__init__`의 self를 제외한 매개변수.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > name = 'claude'
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/integrations/factory.py:14` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/factory.py:15` — `_live_llm` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:52` — `ClaudeLLM.__init__` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:53` — `ClaudeLLM.__init__` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:63` — `ClaudeLLM._call` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:64` — `ClaudeLLM._call` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:110` — `ClaudeLLM.answer` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:114` — `ClaudeLLM.answer` / 참조·타입·콜백 등
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 4.1 `ClaudeLLM.__init__`
> > > > > > - 4.2 `ClaudeLLM._call`
> > > > > > - 4.3 `ClaudeLLM.answer`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>4.1. [초기화 메서드] ClaudeLLM.__init__</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > > >
> > > > > > > **소속 클래스:** `ClaudeLLM`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:42`
> > > > > > > - **역할·로직:** SDK 설치와 API 키를 확인한 뒤 Anthropic 클라이언트와 사용할 모델 이름을 저장합니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `None`
> > > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def __init__(self) -> None:
> > > > > > > >         try:
> > > > > > > >             from anthropic import Anthropic
> > > > > > > >         except ImportError as exc:
> > > > > > > >             raise ExternalServiceError("anthropic 패키지가 설치 되어 있지 않습니다.") from exc
> > > > > > > >
> > > > > > > >         settings = get_settings() 
> > > > > > > >         key = settings.anthropic_api_key  # SecretStr | None 값이 비어있을 수도 있다. 
> > > > > > > >         if key is None:
> > > > > > > >             raise ExternalServiceError("ANTHROPIC_API_KEY 가 비어있습니다.")
> > > > > > > >         self._client = Anthropic(api_key=key.get_secret_value()) 
> > > > > > > >         self._model = settings.llm_model
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - 이 클래스의 객체 생성 시 자동 호출됩니다. 호출·사용 위치는 위 클래스 항목에도 나열합니다. self는 파이썬이 자동 전달합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/core/exceptions.py:7` — `AgentError.__init__` / 대상 확인 필요: super().__init__
> > > > > > > - `FastApi/backend/app/core/exceptions.py:59` — `AuthFailed.__int__` / 대상 확인 필요: super().__init__
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>4.2. [인스턴스 메서드] ClaudeLLM._call</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > > >
> > > > > > > **소속 클래스:** `ClaudeLLM`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:56`
> > > > > > > - **역할·로직:** Claude Messages API를 호출하고 텍스트·사용량·경과 시간을 추출합니다. 호출 오류를 ExternalServiceError로 바꿉니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > > | `system` | `str` | `필수` | `위치/키워드` | Claude에 전달할 시스템 지침 |
> > > > > > > | `user_text` | `str` | `필수` | `위치/키워드` | Claude에 전달할 사용자 메시지 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `tuple[str, dict, int]`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return (text, usage, elapsed)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def _call(self, system: str, user_text: str) -> tuple[str, dict, int]:
> > > > > > > >         # system : 시스템 프롬프트 한 덩어리 
> > > > > > > >         # user_text : 사용자 메세지 본문 
> > > > > > > >
> > > > > > > >         started = time.perf_counter()  # 시간차이 구하는 기능 
> > > > > > > >         # claude api 호출 
> > > > > > > >         try:
> > > > > > > >             response = self._client.messages.create(
> > > > > > > >                 model=self._model, 
> > > > > > > >                 max_tokens=get_settings().max_token, 
> > > > > > > >                 system=system,
> > > > > > > >                 messages=[{"role": "user", "content": user_text}],
> > > > > > > >             )
> > > > > > > >         except Exception as exc: 
> > > > > > > >             log.exception("Claude 호출 실패")
> > > > > > > >             # 상위 코드는 Claude 전용 예외 대신 우리 프로젝트의 예외만 알면 된다.
> > > > > > > >             raise ExternalServiceError(f"Claude 호출에 실패했습니다: {exc}") from exc
> > > > > > > >
> > > > > > > >         # * 응답 받은 내용중 필요한 부분만 추출해서 우리 규격으로 만들기 *
> > > > > > > >         # 응답 텍스트 꺼내기 
> > > > > > > >         text = "".join(b.text for b in response.content if getattr(b, "type", "") == "text")
> > > > > > > >         """
> > > > > > > >         parts = []
> > > > > > > >
> > > > > > > >         for block in response.content:
> > > > > > > >             if getattr(block, "type", "") == "text":
> > > > > > > >                 parts.append(block.text)
> > > > > > > >
> > > > > > > >         text = "".join(parts)
> > > > > > > >         """
> > > > > > > >         usg = response.usage  # 사용량 정보 꺼내기 
> > > > > > > >         # 사용량 정보 정리 
> > > > > > > >         usage = {
> > > > > > > >             "input": getattr(usg, "input_tokens", 0) or 0, 
> > > > > > > >             "cache_read": getattr(usg, "cache_read_input_tokens", 0) or 0, 
> > > > > > > >             "cache_write": getattr(usg, "cache_creation_input_tokens", 0) or 0, 
> > > > > > > >             "output": getattr(usg, "output_tokens", 0) or 0,
> > > > > > > >         }
> > > > > > > >         # 걸린 시간 계산 
> > > > > > > >         elapsed = int((time.perf_counter() - started) * 1000) 
> > > > > > > >         # 결과 리턴 
> > > > > > > >         return text, usage, elapsed
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - `FastApi/backend/app/integrations/llm_claude.py:110` — `ClaudeLLM.answer` / 직접 호출
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>4.3. [인스턴스 메서드] ClaudeLLM.answer</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > > >
> > > > > > > **소속 클래스:** `ClaudeLLM`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:100`
> > > > > > > - **역할·로직:** 시스템 프롬프트·사용자·근거·질문을 구성하고 _call을 실행한 뒤 토큰·비용을 LLMResult에 담습니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > > | `question` | `str` | `필수` | `키워드 전용` | 사용자 질문 또는 재시도 힌트가 포함된 질문 |
> > > > > > > | `contexts` | `list[dict]` | `필수` | `키워드 전용` | 모델에게 전달할 근거 문서 dict 목록 |
> > > > > > > | `user` | `dict` | `필수` | `키워드 전용` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `LLMResult`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return LLMResult(text=text, model=self._model, input_tok=total_in, cache_tok=usage['cache_read'], output_tok=usage['output'], cost_krw=estimate_cost_krw(total_in, usage['output']), latency_ms=ms)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def answer(self, *, question: str, contexts: list[dict], user: dict) -> LLMResult: 
> > > > > > > >         # question : 사용자 질문 
> > > > > > > >         # contexts : 근거 문서 목록. 
> > > > > > > >         # user : 질문한 사람. 
> > > > > > > >         system = _load_prompt("answer_system.md") 
> > > > > > > >         prompt = (
> > > > > > > >             f"## 사용자\n{user.get('name')} - {user.get('dept')}\n\n"
> > > > > > > >             f"## 근거 문서\n{_cotext_block(contexts)}\n\n"
> > > > > > > >             f"## 질문\n{question}"
> > > > > > > >         )
> > > > > > > >         text, usage, ms = self._call(system, prompt) # 위 _call 함수 불러서 호출하고 리턴데이터 받기 
> > > > > > > >         total_in = usage["input"] + usage["cache_read"] + usage["cache_write"] # 입력토큰 합계 
> > > > > > > >         return LLMResult(
> > > > > > > >             text=text, 
> > > > > > > >             model=self._model,
> > > > > > > >             input_tok=total_in,
> > > > > > > >             cache_tok=usage["cache_read"],
> > > > > > > >             output_tok=usage["output"],
> > > > > > > >             cost_krw=estimate_cost_krw(total_in, usage["output"]),
> > > > > > > >             latency_ms=ms
> > > > > > > >         )
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastApi/backend/app/services/chat_service.py의 ask가 llm.answer(...)로 호출합니다. live에서는 FastApi/backend/app/integrations/factory.py가 반환한 ClaudeLLM.answer, 골든셋에서는 FastApi/backend/tests/test_chat_golden.py의 StubLLM.answer가 실행됩니다. LLMPort.answer 본문이 대신 실행되는 구조는 아닙니다. FastApi/backend/app/agent/chain.py의 call_port에도 같은 포트 호출이 있습니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/agent/chain.py:59` — `build_result_chain.call_port` / 대상 확인 필요: llm.answer
> > > > > > > - `FastApi/backend/app/services/chat_service.py:112` — `ask` / 대상 확인 필요: llm.answer
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>5. [독립 함수] _extract_json</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/llm_claude.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/llm_claude.py:123`
> > > > > > - **역할·로직:** 코드 펜스와 앞뒤 설명을 걷어내 JSON 객체를 해석합니다. 중괄호가 없거나 JSON 해석 실패 시 빈 dict입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {}
> > > > > > return json.loads(raw[start:end + 1])
> > > > > > return {}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _extract_json(text: str) -> dict:
> > > > > > >     # 정규 표현식으로 원하는 부분만 추출 
> > > > > > >     fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
> > > > > > >     raw = fenced.group(1) if fenced else text
> > > > > > >
> > > > > > >     # 펜스가 없으면 앞뒤에 설명 문장이 붙어 있을 수 있다. 첫 { 와 마지막 } 사이만 남긴다.
> > > > > > >     start, end = raw.find("{"), raw.rfind("}")
> > > > > > >     if start == -1 or end == -1:
> > > > > > >         return {}
> > > > > > >     try:
> > > > > > >         return json.loads(raw[start : end + 1])
> > > > > > >     except json.JSONDecodeError:
> > > > > > >         log.warning("응답 JSON 파싱 실패")
> > > > > > >         return {}
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:82` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:118` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/integrations/ports.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `LLMResult`, `LLMPort`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] LLMResult</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/ports.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/ports.py:8`
> > > > > > - **역할·로직:** 답변 문자열과 모델명·사용량·비용·시간을 담는 dataclass입니다.
> > > > > > - **데코레이터:** `dataclass`
> > > > > > - **상속:** 명시적 부모 없음(object)
> > > > > > - **클래스 호출 결과:** `LLMResult` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드들로 dataclass가 __init__을 자동 생성합니다. 기본값 없는 필드는 필수입니다. extras의 default_factory는 객체마다 새 dict를 만듭니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > text: str
> > > > > > model: str
> > > > > > input_tok: int = 0
> > > > > > cache_tok: int = 0
> > > > > > output_tok: int = 0
> > > > > > cost_krw: float = 0.0
> > > > > > latency_ms: int = 0
> > > > > > extras: dict = field(default_factory=dict)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:15` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/agent/chain.py:56` — `build_result_chain.call_port` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:100` — `ClaudeLLM.answer` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/llm_claude.py:112` — `ClaudeLLM.answer` / 직접 호출
> > > > > > - `FastApi/backend/app/integrations/ports.py:21` — `LLMPort.answer` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:11` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:26` — `StubLLM.answer` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:30` — `StubLLM.answer` / 직접 호출
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] LLMPort</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/integrations/ports.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/integrations/ports.py:20`
> > > > > > - **역할·로직:** answer의 입력과 반환 타입을 정의하는 Protocol입니다. 실제 모델 호출을 구현하지 않습니다.
> > > > > > - **데코레이터:** `runtime_checkable`
> > > > > > - **상속:** `Protocol`
> > > > > > - **클래스 호출 결과:** Protocol 규약이며 직접 인스턴스화하는 클래스가 아닙니다.
> > > > > > - **직접 정의한 메서드:** `answer`
> > > > > > - **생성 매개변수:** 직접 정의한 __init__ 없음. 부모가 있으면 부모 규칙을 따릅니다. Protocol은 구현 어댑터 대신 생성해 쓰는 대상이 아닙니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:15` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/agent/chain.py:42` — `build_result_chain` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/agent/chain.py:66` — `build_answer_chain` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/agent/chain.py:71` — `build_parsed_chain` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/factory.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/integrations/factory.py:12` — `_live_llm` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/integrations/factory.py:18` — `get_llm` / 참조·타입·콜백 등
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 2.1 `LLMPort.answer`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2.1. [인스턴스 메서드] LLMPort.answer</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/integrations/ports.py`
> > > > > > >
> > > > > > > **소속 클래스:** `LLMPort`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/integrations/ports.py:21`
> > > > > > > - **역할·로직:** 어댑터가 제공할 answer 메서드의 규격만 선언합니다. 본문은 ...입니다.
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > > | `question` | `str` | `필수` | `키워드 전용` | 사용자 질문 또는 재시도 힌트가 포함된 질문 |
> > > > > > > | `contexts` | `list[dict]` | `필수` | `키워드 전용` | 모델에게 전달할 근거 문서 dict 목록 |
> > > > > > > | `user` | `dict` | `필수` | `키워드 전용` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `LLMResult`
> > > > > > > - 규약상 LLMResult입니다. 이 선언 자체는 실제 모델 응답을 생성하지 않습니다. 구현 어댑터가 반환합니다.
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def answer(self, *, question: str, contexts: list[dict], user: dict) -> LLMResult: ...
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - FastApi/backend/app/services/chat_service.py의 ask가 llm.answer(...)로 호출합니다. live에서는 FastApi/backend/app/integrations/factory.py가 반환한 ClaudeLLM.answer, 골든셋에서는 FastApi/backend/tests/test_chat_golden.py의 StubLLM.answer가 실행됩니다. LLMPort.answer 본문이 대신 실행되는 구조는 아닙니다. FastApi/backend/app/agent/chain.py의 call_port에도 같은 포트 호출이 있습니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/agent/chain.py:59` — `build_result_chain.call_port` / 대상 확인 필요: llm.answer
> > > > > > > - `FastApi/backend/app/services/chat_service.py:112` — `ask` / 대상 확인 필요: llm.answer
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/models</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/base.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `Base`, `TimestampMixin`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] Base</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/base.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/base.py:6`
> > > > > > - **역할·로직:** SQLAlchemy 선언형 모델의 공통 부모입니다.
> > > > > > - **상속:** `DeclarativeBase`
> > > > > > - **클래스 호출 결과:** `Base` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 직접 정의한 __init__ 없음. 부모가 있으면 부모 규칙을 따릅니다. Protocol은 구현 어댑터 대신 생성해 쓰는 대상이 아닙니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/init_db.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/init_db.py:8` — `init_db` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/migrations/env.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/migrations/env.py:28` — `모듈 실행부` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/__init__.py:2` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:8` — `Document` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/document.py:34` — `DocumentVersion` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/org.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/org.py:12` — `Department` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/org.py:23` — `User` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/run.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/run.py:10` — `Run` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/run.py:25` — `RunStep` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/usage.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/usage.py:11` — `UsageLog` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] TimestampMixin</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/base.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/base.py:9`
> > > > > > - **역할·로직:** 생성·수정 시각 컬럼을 모델에 더하는 믹스인입니다.
> > > > > > - **상속:** 명시적 부모 없음(object)
> > > > > > - **클래스 호출 결과:** `TimestampMixin` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 직접 정의한 __init__ 없음. 부모가 있으면 부모 규칙을 따릅니다. Protocol은 구현 어댑터 대신 생성해 쓰는 대상이 아닙니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > created_at: Mapped[datetime] = mapped_column(default=datetime.now)
> > > > > > updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/models/__init__.py:2` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:8` — `Document` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/document.py:34` — `DocumentVersion` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/org.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/org.py:12` — `Department` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/org.py:23` — `User` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/run.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/run.py:10` — `Run` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/usage.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/usage.py:11` — `UsageLog` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/document.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `Document`, `DocumentVersion`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] Document</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/document.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/document.py:8`
> > > > > > - **역할·로직:** documents 테이블의 문서 기본정보와 버전 관계를 나타냅니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `Document` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `current`
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'documents'
> > > > > > id: Mapped[str] = mapped_column(String(20), primary_key=True)
> > > > > > title: Mapped[str] = mapped_column(String(200))
> > > > > > dept_id: Mapped[str] = mapped_column(ForeignKey('departments.id'), index=True)
> > > > > > security_level: Mapped[str] = mapped_column(String(10), index=True)
> > > > > > owner_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
> > > > > > dept: Mapped['Department'] = relationship(back_populates='documents')
> > > > > > owner: Mapped['User | None'] = relationship(back_populates='documents')
> > > > > > versions: Mapped[list['DocumentVersion']] = relationship(back_populates='document', order_by='DocumentVersion.version')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:17` — `count_rows` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/seed.py:31` — `_seed` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/seed.py:44` — `_seed` / 직접 호출
> > > > > > - `FastApi/backend/app/models/__init__.py:3` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:28` — `Document.current` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:19` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:20` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:24` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:26` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:34` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:39` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:42` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:46` — `get_document` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:47` — `get_document` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:49` — `add_version` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/document_service.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/document_service.py:14` — `_to_out` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/document_service.py:82` — `create_document` / 직접 호출
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 1.1 `Document.current`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>1.1. [속성 메서드] Document.current</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/models/document.py`
> > > > > > >
> > > > > > > **소속 클래스:** `Document`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/models/document.py:27`
> > > > > > > - **역할·로직:** 문서 버전 목록에서 상태가 현행인 첫 버전을 찾습니다. 없으면 None입니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `'DocumentVersion \| None'`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return v
> > > > > > > return None
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def current(self) -> "DocumentVersion | None":
> > > > > > > >         for v in self.versions:
> > > > > > > >             if v.status == "현행":
> > > > > > > >                 return v
> > > > > > > >         return None
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.current처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > > >
> > > > > > > - `FastApi/backend/app/services/document_service.py:59` — `get_document` / 대상 확인 필요: document.current
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] DocumentVersion</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/document.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/document.py:34`
> > > > > > - **역할·로직:** document_versions 테이블의 개별 문서 버전·유효기간·색인 상태를 나타냅니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `DocumentVersion` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `period`, `is_searchable`
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'document_versions'
> > > > > > id: Mapped[int] = mapped_column(primary_key=True)
> > > > > > doc_id: Mapped[str] = mapped_column(ForeignKey('documents.id'), index=True)
> > > > > > version: Mapped[str] = mapped_column(String(10))
> > > > > > status: Mapped[str] = mapped_column(String(10))
> > > > > > effective_from: Mapped[date]
> > > > > > expires_at: Mapped[date | None]
> > > > > > file_path: Mapped[str | None] = mapped_column(String(300))
> > > > > > file_format: Mapped[str] = mapped_column(String(10))
> > > > > > chunk_count: Mapped[int] = mapped_column(default=0)
> > > > > > embed_model: Mapped[str | None] = mapped_column(String(50))
> > > > > > index_status: Mapped[str] = mapped_column(String(10), default='대기')
> > > > > > index_progress: Mapped[int] = mapped_column(default=0)
> > > > > > indexed_at: Mapped[date | None]
> > > > > > document: Mapped['Document'] = relationship(back_populates='versions')
> > > > > > __table_args__ = (UniqueConstraint('doc_id', 'version', name='uq_doc_version'),)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:18` — `count_rows` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/seed.py:47` — `_seed` / 직접 호출
> > > > > > - `FastApi/backend/app/models/__init__.py:3` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/document.py:61` — `DocumentVersion.period` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/document.py:62` — `DocumentVersion.period` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/document.py:63` — `DocumentVersion.period` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/document.py:67` — `DocumentVersion.is_searchable` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:19` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:20` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:28` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:42` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:49` — `add_version` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/document_repo.py:50` — `add_version` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:10` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/document_service.py:14` — `_to_out` / 참조·타입·콜백 등
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 2.1 `DocumentVersion.period`
> > > > > > - 2.2 `DocumentVersion.is_searchable`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2.1. [속성 메서드] DocumentVersion.period</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/models/document.py`
> > > > > > >
> > > > > > > **소속 클래스:** `DocumentVersion`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/models/document.py:60`
> > > > > > > - **역할·로직:** 문서 버전의 시행일과 만료일을 표시할 문자열로 만듭니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `str`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return f'{self.effective_from} ~'
> > > > > > > return f'{self.effective_from} ~ {self.expires_at}'
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def period(self) -> str:
> > > > > > > >         if self.expires_at is None:
> > > > > > > >             return f"{self.effective_from} ~"
> > > > > > > >         return f"{self.effective_from} ~ {self.expires_at}"
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.period처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2.2. [속성 메서드] DocumentVersion.is_searchable</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/models/document.py`
> > > > > > >
> > > > > > > **소속 클래스:** `DocumentVersion`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/models/document.py:66`
> > > > > > > - **역할·로직:** 버전 상태가 현행이고 색인 상태가 완료인지 판단합니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `bool`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return self.status == '현행' and self.index_status == '완료'
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def is_searchable(self) -> bool:
> > > > > > > >         return self.status == "현행" and self.index_status == "완료"
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.is_searchable처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/org.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `Department`, `User`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] Department</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/org.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/org.py:12`
> > > > > > - **역할·로직:** departments 테이블의 부서 모델입니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `Department` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'departments'
> > > > > > id: Mapped[str] = mapped_column(String(10), primary_key=True)
> > > > > > name: Mapped[str] = mapped_column(String(50), unique=True)
> > > > > > users: Mapped[list['User']] = relationship(back_populates='dept')
> > > > > > documents: Mapped[list['Document']] = relationship(back_populates='dept')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:15` — `count_rows` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/seed.py:34` — `_seed` / 직접 호출
> > > > > > - `FastApi/backend/app/models/__init__.py:4` — `모듈 import` / import/재공개
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] User</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/org.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/org.py:23`
> > > > > > - **역할·로직:** users 테이블의 사용자 모델입니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `User` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** `clearance_level`, `can_approve`
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'users'
> > > > > > id: Mapped[int] = mapped_column(primary_key=True)
> > > > > > emp_no: Mapped[str] = mapped_column(String(16), unique=True, index=True)
> > > > > > name: Mapped[str] = mapped_column(String(50))
> > > > > > dept_id: Mapped[str] = mapped_column(ForeignKey('departments.id'))
> > > > > > role: Mapped[str] = mapped_column(String(10))
> > > > > > clearance: Mapped[str] = mapped_column(String(10))
> > > > > > password_hash: Mapped[str] = mapped_column(String(100), default='')
> > > > > > dept: Mapped['Department'] = relationship(back_populates='users')
> > > > > > documents: Mapped[list['Document']] = relationship(back_populates='owner')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/db/seed.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/db/seed.py:16` — `count_rows` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/db/seed.py:38` — `_seed` / 직접 호출
> > > > > > - `FastApi/backend/app/models/__init__.py:4` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/models/org.py:38` — `User.clearance_level` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/models/org.py:43` — `User.can_approve` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/user_repo.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/repositories/user_repo.py:8` — `get_by_emp_no` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/repositories/user_repo.py:9` — `get_by_emp_no` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/auth_service.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/auth_service.py:10` — `_to_out` / 참조·타입·콜백 등
> > > > > >
> > > > > > **이 클래스의 메서드**
> > > > > >
> > > > > > - 2.1 `User.clearance_level`
> > > > > > - 2.2 `User.can_approve`
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2.1. [속성 메서드] User.clearance_level</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/models/org.py`
> > > > > > >
> > > > > > > **소속 클래스:** `User`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/models/org.py:37`
> > > > > > > - **역할·로직:** 사용자 보안 등급을 숫자로 바꾸고 알 수 없는 값이면 1을 사용합니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `int`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return CLEARANCE.get(self.clearance, 1)
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def clearance_level(self) -> int:
> > > > > > > >         return CLEARANCE.get(self.clearance, 1)
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.clearance_level처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > <details>
> > > > > > <summary><h2>2.2. [속성 메서드] User.can_approve</h2></summary>
> > > > > > >
> > > > > > > **소속 파일:** `FastApi/backend/app/models/org.py`
> > > > > > >
> > > > > > > **소속 클래스:** `User`
> > > > > > >
> > > > > > > - **정의 파일:** `FastApi/backend/app/models/org.py:41`
> > > > > > > - **역할·로직:** 사용자 역할이 팀장 또는 관리자인지 확인합니다.
> > > > > > > - **데코레이터:** `property`
> > > > > > >
> > > > > > > **매개변수**
> > > > > > >
> > > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > > | --- | --- | --- | --- | --- |
> > > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > >
> > > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > > >
> > > > > > > **반환값**
> > > > > > >
> > > > > > > - 선언: `bool`
> > > > > > > - 실제 return 표현식(분기별):
> > > > > > >
> > > > > > > ```python
> > > > > > > return self.role in {'팀장', '관리자'}
> > > > > > > ```
> > > > > > >
> > > > > > > <details>
> > > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > > >
> > > > > > > > ```python
> > > > > > > > def can_approve(self) -> bool:
> > > > > > > >
> > > > > > > >         return self.role in {"팀장", "관리자"}
> > > > > > > > ```
> > > > > > > >
> > > > > > > </details>
> > > > > > >
> > > > > > > **자동 호출·사용 방식**
> > > > > > >
> > > > > > > - @property이므로 obj.can_approve처럼 속성을 읽을 때 실행합니다. 아래 동명 속성 참조 후보는 객체 타입을 별도로 확인해야 합니다.
> > > > > > >
> > > > > > > **호출·사용 위치**
> > > > > > >
> > > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/run.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `Run`, `RunStep`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] Run</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/run.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/run.py:10`
> > > > > > - **역할·로직:** runs 테이블의 질문 한 건 실행 기록입니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `Run` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'runs'
> > > > > > id: Mapped[str] = mapped_column(String(32), primary_key=True)
> > > > > > user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
> > > > > > question: Mapped[str] = mapped_column(Text, nullable=False)
> > > > > > answer: Mapped[str | None] = mapped_column(Text, nullable=True)
> > > > > > status: Mapped[str] = mapped_column(String(24), default='완료')
> > > > > > latency_ms: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > mode: Mapped[str] = mapped_column(String(8), default='mock')
> > > > > > sources: Mapped[list | None] = mapped_column(JSON, nullable=True)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/models/__init__.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:14` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:90` — `ask` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:138` — `ask` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/chat_service.py:149` — `get_run` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/ids.py:5` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/ids.py:12` — `next_run_id` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] RunStep</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/run.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/run.py:25`
> > > > > > - **역할·로직:** run_steps 테이블의 실행 안 단계 한 건입니다.
> > > > > > - **상속:** `Base`
> > > > > > - **클래스 호출 결과:** `RunStep` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'run_steps'
> > > > > > id: Mapped[int] = mapped_column(primary_key=True)
> > > > > > run_id: Mapped[str] = mapped_column(ForeignKey('runs.id'), nullable=False)
> > > > > > ord: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > name: Mapped[str] = mapped_column(String(64))
> > > > > > ok: Mapped[bool] = mapped_column(default=True)
> > > > > > ms: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > detail: Mapped[str | None] = mapped_column(Text, nullable=True)
> > > > > > ```
> > > > > >
> > > > > > **자동 호출·사용 방식**
> > > > > >
> > > > > > - FastApi/backend/app/models/__init__.py에서 공개되지만 현재 FastApi/backend/app/services/chat_service.py에 RunStep을 생성·저장하는 호출은 없습니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/models/__init__.py:5` — `모듈 import` / import/재공개
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/models/usage.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `UsageLog`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] UsageLog</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/models/usage.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/models/usage.py:11`
> > > > > > - **역할·로직:** usage_logs 테이블의 모델 호출 한 번의 토큰·비용 기록입니다.
> > > > > > - **상속:** `Base`, `TimestampMixin`
> > > > > > - **클래스 호출 결과:** `UsageLog` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** SQLAlchemy가 제공하는 키워드 생성자로 아래 매핑 속성을 지정합니다. Python 인자의 필수 여부와 DB의 nullable/default/PK 제약은 별개입니다.
> > > > > > - **자동 기능:** Base의 ORM 매핑 기능을 상속합니다. TimestampMixin을 상속하면 FastApi/backend/app/models/base.py의 created_at, updated_at도 포함합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > __tablename__ = 'usage_logs'
> > > > > > id: Mapped[int] = mapped_column(primary_key=True)
> > > > > > run_id: Mapped[str] = mapped_column(ForeignKey('runs.id'), nullable=False)
> > > > > > model: Mapped[str] = mapped_column(String(64))
> > > > > > input_tok: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > cache_tok: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > output_tok: Mapped[int] = mapped_column(Integer, default=0)
> > > > > > cost_krw: Mapped[float] = mapped_column(Float, default=0.0)
> > > > > > occurred_at: Mapped[datetime] = mapped_column(default=datetime.now)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/models/__init__.py:6` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:14` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:61` — `_record_usage` / 직접 호출
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/repositories</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/repositories/document_repo.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `list_documents`, `get_document`, `add_version`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] list_documents</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/repositories/document_repo.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/repositories/document_repo.py:9`
> > > > > > - **역할·로직:** 문서 목록을 필터 조건으로 조회하는 SQLAlchemy DB 작업입니다. 목록은 버전과 문서의 행 조합, 단건은 Document 또는 None입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > > | `dept_id` | `str \| None` | `None` | `키워드 전용` | 부서 식별자 또는 필터 |
> > > > > > | `security_level` | `str \| None` | `None` | `키워드 전용` | 문서 보안 등급 또는 필터 |
> > > > > > | `status` | `str \| None` | `None` | `키워드 전용` | 문서 상태 필터 또는 테스트의 기대 HTTP 상태 코드 |
> > > > > > | `q` | `str \| None` | `None` | `키워드 전용` | 문서 제목·ID 검색어 |
> > > > > > | `limit` | `int` | `50` | `키워드 전용` | 최대 조회 건수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `list[Row]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return list(session.execute(stmt).all())
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def list_documents(
> > > > > > >     session: Session,
> > > > > > >     *,
> > > > > > >     dept_id: str | None = None,
> > > > > > >     security_level: str | None = None,
> > > > > > >     status: str | None = None,
> > > > > > >     q: str | None = None,
> > > > > > >     limit: int = 50,
> > > > > > > ) -> list[Row]:
> > > > > > >
> > > > > > >     stmt = select(DocumentVersion, Document).join(
> > > > > > >         Document, DocumentVersion.doc_id == Document.id
> > > > > > >     )
> > > > > > >
> > > > > > >     if dept_id:
> > > > > > >         stmt = stmt.where(Document.dept_id == dept_id)
> > > > > > >     if security_level:
> > > > > > >         stmt = stmt.where(Document.security_level == security_level)
> > > > > > >     if status:
> > > > > > >         stmt = stmt.where(DocumentVersion.status == status)
> > > > > > >     if q:
> > > > > > >         
> > > > > > >         
> > > > > > >         
> > > > > > >         stmt = stmt.where(
> > > > > > >             or_(Document.title.ilike(f"%{q}%"), Document.id.ilike(f"%{q}%"))
> > > > > > >         )
> > > > > > >
> > > > > > >     
> > > > > > >     
> > > > > > >     stmt = stmt.options(joinedload(Document.dept))
> > > > > > >
> > > > > > >     
> > > > > > >     stmt = stmt.order_by(Document.id, desc(DocumentVersion.version)).limit(limit)
> > > > > > >     return list(session.execute(stmt).all())
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/document_service.py:41` — `list_documents` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] get_document</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/repositories/document_repo.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/repositories/document_repo.py:46`
> > > > > > - **역할·로직:** 문서 한 건을 조회하는 SQLAlchemy DB 작업입니다. 목록은 버전과 문서의 행 조합, 단건은 Document 또는 None입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > > | `doc_id` | `str` | `필수` | `위치/키워드` | 문서 식별자 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `Document \| None`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return session.get(Document, doc_id)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_document(session: Session, doc_id: str) -> Document | None:
> > > > > > >     return session.get(Document, doc_id)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/document_service.py:56` — `get_document` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:79` — `create_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] add_version</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/repositories/document_repo.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/repositories/document_repo.py:49`
> > > > > > - **역할·로직:** 문서에 연결할 DocumentVersion을 추가하고 flush한 뒤 객체를 반환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > > | `doc` | `Document` | `필수` | `위치/키워드` | 버전을 추가할 Document 객체 |
> > > > > > | `**fields` | `타입 표기 없음` | `0개 이상` | `추가 키워드 인자` | 새 문서 버전에 넣을 추가 필드 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `DocumentVersion`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return version
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def add_version(session: Session, doc: Document, **fields) -> DocumentVersion:
> > > > > > >     version = DocumentVersion(doc_id=doc.id, **fields)
> > > > > > >     session.add(version)
> > > > > > >     session.flush()
> > > > > > >     return version
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/document_service.py:97` — `create_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/repositories/user_repo.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `get_by_emp_no`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] get_by_emp_no</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/repositories/user_repo.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/repositories/user_repo.py:8`
> > > > > > - **역할·로직:** 사번이 일치하는 사용자를 부서와 함께 조회합니다. 없으면 None입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > > | `emp_no` | `str` | `필수` | `위치/키워드` | 사용자 사번 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `User \| None`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return session.scalars(stmt).first()
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_by_emp_no(session: Session, emp_no: str) -> User | None:
> > > > > > >     stmt = select(User).where(User.emp_no == emp_no).options(joinedload(User.dept)) # department 테이블 정보도 조인해서 함께 가져와
> > > > > > >     return session.scalars(stmt).first()
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/auth_service.py:24` — `authenticate` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:34` — `get_me` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/schemas</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/schemas/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/schemas/auth.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `LoginIn`, `UserOut`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] LoginIn</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/auth.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/auth.py:6`
> > > > > > - **역할·로직:** 로그인 요청 본문의 사번과 비밀번호 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `LoginIn` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > emp_no: str = Field(examples=['2016-0231'])
> > > > > > password: str = Field(min_length=1)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/auth.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/auth.py:17` — `login` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] UserOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/auth.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/auth.py:11`
> > > > > > - **역할·로직:** 사용자 정보 응답 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `UserOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > id: int
> > > > > > emp_no: str = Field(examples=['2016-0231'])
> > > > > > name: str
> > > > > > dept: str = Field(examples=['인사총무'])
> > > > > > role: Literal['일반', '팀장', '관리자']
> > > > > > clearance: Literal['일반', '3급', '대외비']
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/auth.py:9` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/auth.py:16` — `login` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/api/v1/auth.py:22` — `me` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/schemas/chat.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `ChatRequest`, `AnswerSource`, `AnswerOut`, `AskOut`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] ChatRequest</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/chat.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/chat.py:10`
> > > > > > - **역할·로직:** 사용자의 질문 입력 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `ChatRequest` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > question: str = Field(min_length=2, max_length=2000, description='사용자 질문. 두 글자 이상 2000자 이하')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/chat.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/chat.py:14` — `create_message` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] AnswerSource</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/chat.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/chat.py:18`
> > > > > > - **역할·로직:** 인용 출처 한 건의 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `AnswerSource` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > doc_id: DOC_IDS = Field(description='인용한 문서 번호. 등록된 세 건 중 하나')
> > > > > > title: str = Field(description='문서 제목')
> > > > > > version: str = Field(description='문서 버전. 예: v2.0')
> > > > > > locator: str = Field(description='문서 안 위치. 예: 제12조 - p.6')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/schemas/chat.py:27` — `AnswerOut` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [클래스] AnswerOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/chat.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/chat.py:25`
> > > > > > - **역할·로직:** 답변·출처 목록·근거 충분 여부의 검증 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `AnswerOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > answer: str = Field(description='한국어 답변 본문')
> > > > > > sources: list[AnswerSource] = Field(description='답변이 인용한 근거 목록')
> > > > > > enough_evidence: bool = Field(description='근거가 충분했는가. 부족하면 False')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/schemas/chat.py:32` — `AskOut` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/chat_service.py:16` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:119` — `ask` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [클래스] AskOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/chat.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/chat.py:32`
> > > > > > - **역할·로직:** AnswerOut에 실행 번호·시도 횟수·폴백 여부를 추가한 최종 응답 규격입니다.
> > > > > > - **상속:** `AnswerOut`
> > > > > > - **클래스 호출 결과:** `AskOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > > - **상속 필드:** FastApi/backend/app/schemas/chat.py의 AnswerOut에 있는 answer, sources, enough_evidence.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > run_id: str = Field(description='이 질문 한 건의 실행 번호.예: RUN-1234')
> > > > > > attempts: int = Field(default=1, description='스키마 검증에 성공하기까지 부른 횟수')
> > > > > > fallback_used: bool = Field(default=False, description='세 번 모두 실패해 폴백 답변으로 대처한 여부')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/chat.py:7` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/chat.py:13` — `create_message` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/api/v1/chat.py:14` — `create_message` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/chat_service.py:16` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:43` — `_fallback` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/chat_service.py:45` — `_fallback` / 직접 호출
> > > > > > - `FastApi/backend/app/services/chat_service.py:73` — `ask` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/services/chat_service.py:127` — `ask` / 직접 호출
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/schemas/common.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `HealthOut`, `ErrorOut`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] HealthOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/common.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/common.py:4`
> > > > > > - **역할·로직:** 상태 확인 응답 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `HealthOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > status: str
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] ErrorOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/common.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/common.py:7`
> > > > > > - **역할·로직:** 오류 응답 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `ErrorOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > code: str
> > > > > > message: str
> > > > > > detail: str | None = None
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/schemas/document.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: `DocumentOut`, `DocumentCreateOut`
> > > > > - 파일 수준 함수: 없음
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [클래스] DocumentOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/document.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/document.py:7`
> > > > > > - **역할·로직:** 문서 조회 응답 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `DocumentOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > doc_id: str
> > > > > > title: str
> > > > > > dept: str
> > > > > > version: str
> > > > > > security_level: Literal['일반', '3급', '대외비']
> > > > > > file_format: Literal['docx', 'pdf']
> > > > > > status: Literal['현행', '만료']
> > > > > > effective_from: date
> > > > > > expires_at: date | None = None
> > > > > > index_status: Literal['대기', '재임베딩', '완료', '보관'] = '대기'
> > > > > > index_progress: int = Field(default=0, ge=0, le=100)
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/documents.py:26` — `list_documents` / 참조·타입·콜백 등
> > > > > > - `FastApi/backend/app/api/v1/documents.py:86` — `get_document` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [클래스] DocumentCreateOut</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/schemas/document.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/schemas/document.py:23`
> > > > > > - **역할·로직:** 문서 생성 응답 규격입니다.
> > > > > > - **상속:** `BaseModel`
> > > > > > - **클래스 호출 결과:** `DocumentCreateOut` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > > - **직접 정의한 메서드:** 없음
> > > > > > - **생성 매개변수:** 아래 필드 이름을 키워드 인자로 받습니다. 기본값 없는 필드는 필수이며, 상속 필드도 포함합니다. BaseSettings는 환경설정에서도 값을 읽습니다.
> > > > > > - **상속 메서드:** model_validate로 데이터를 검증하고 model_dump로 dict를 만들 수 있습니다. 프로젝트가 직접 작성한 메서드는 아래에만 나열합니다.
> > > > > >
> > > > > > **필드·클래스 속성 선언**
> > > > > >
> > > > > > ```python
> > > > > > doc_id: str = Field(examples=['DOC-HR-014'])
> > > > > > title: str
> > > > > > version: str = Field(examples=['v2.0'])
> > > > > > file_format: Literal['docx', 'pdf']
> > > > > > file_path: str = Field(examples=['uploads/DOC-HR-014_v2.0.docx'])
> > > > > > created: bool = Field(description='문서 자체가 이번에 새로 생겼으면 True, 버전만 더했으면 False')
> > > > > > ```
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:8` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/api/v1/documents.py:45` — `upload_document` / 참조·타입·콜백 등
> > > > > >
> > > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/app/services</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/services/__init__.py</h1></summary>
> > > > >
> > > > > 직접 정의한 함수·클래스: **없음**.
> > > > >
> > > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/services/auth_service.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `_to_out`, `authenticate`, `get_me`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] _to_out</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/auth_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/auth_service.py:10`
> > > > > > - **역할·로직:** ORM 사용자 객체를 응답용 dict로 변환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `user` | `User` | `필수` | `위치/키워드` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {'id': user.id, 'emp_no': user.emp_no, 'name': user.name, 'dept': user.dept.name, 'role': user.role, 'clearance': user.clearance}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _to_out(user: User) -> dict:
> > > > > > >     return {
> > > > > > >         "id": user.id,
> > > > > > >         "emp_no": user.emp_no,
> > > > > > >         "name": user.name,
> > > > > > >         "dept": user.dept.name,
> > > > > > >         "role": user.role,
> > > > > > >         "clearance": user.clearance,
> > > > > > >     }
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/auth_service.py:28` — `authenticate` / 직접 호출
> > > > > > - `FastApi/backend/app/services/auth_service.py:37` — `get_me` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] authenticate</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/auth_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/auth_service.py:21`
> > > > > > - **역할·로직:** 사번으로 사용자를 찾고 비밀번호를 검증합니다. 실패하면 AuthFailed, 성공하면 사용자 정보를 반환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `emp_no` | `str` | `필수` | `위치/키워드` | 사용자 사번 |
> > > > > > | `password` | `str` | `필수` | `위치/키워드` | 로그인 입력 비밀번호 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _to_out(user)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def authenticate(emp_no: str, password: str) -> dict:
> > > > > > >     with session_scope() as s:
> > > > > > >         # DB에서 emo_no로 사원 정보 조회.
> > > > > > >         user = user_repo.get_by_emp_no(s, emp_no)
> > > > > > >         # 사번이 없거나 비밀번호가 일치하지 않으면 
> > > > > > >         if user is None or not verify_password(password, user.password_hash): # 입력비번, DB에 암호화된 비번 비교 
> > > > > > >             raise AuthFailed() # 우리가 만든 인증 예외 발생 
> > > > > > >         return _to_out(user)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/auth.py:19` — `login` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] get_me</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/auth_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/auth_service.py:31`
> > > > > > - **역할·로직:** 사번으로 사용자 정보를 조회합니다. 사용자가 없으면 AuthFailed입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `emp_no` | `str` | `필수` | `위치/키워드` | 사용자 사번 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _to_out(user)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_me(emp_no: str) -> dict:
> > > > > > >     with session_scope() as s:
> > > > > > >         # DB에서 emp_no로 사원 정보 조회 
> > > > > > >         user = user_repo.get_by_emp_no(s, emp_no)
> > > > > > >         if user is None:
> > > > > > >             raise AuthFailed()
> > > > > > >         return _to_out(user)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/auth.py:28` — `me` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/services/chat_service.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `_hint_from`, `_fallback`, `_record_usage`, `ask`, `get_run`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] _hint_from</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/chat_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/chat_service.py:34`
> > > > > > - **역할·로직:** 검증 오류의 필드 경로와 메시지를 합쳐 다음 호출에 전달할 힌트를 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `errors` | `list[dict]` | `필수` | `위치/키워드` | Pydantic 검증 오류 목록 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return '/'.join(parts)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _hint_from(errors: list[dict]) -> str:
> > > > > > >     # errors : ValidationError 가 돌려주는 목록 
> > > > > > >     parts = []
> > > > > > >     for err in errors:
> > > > > > >         where = ".".join(str(x) for x in err.get("loc", ())) or "(최상위)"
> > > > > > >         parts.append(f"{where}: {err.get('msg', '')}")
> > > > > > >     return "/".join(parts)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:121` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] _fallback</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/chat_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/chat_service.py:43`
> > > > > > - **역할·로직:** 답변 불가 안내, 빈 출처, fallback_used=True를 가진 AskOut을 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `run_id` | `str` | `필수` | `위치/키워드` | 질문 한 건의 실행 식별자 |
> > > > > > | `attemps` | `int` | `필수` | `위치/키워드` | 폴백까지 수행한 호출 횟수(현재 철자) |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `AskOut`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return AskOut(answer=FALLBACK_ANSWER, sources=[], enough_evidence=False, run_id=run_id, attempts=attemps, fallback_used=True)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _fallback(run_id: str, attemps: int) -> AskOut:
> > > > > > >     # 사용자에게 응답해줄 최종 응답 결과 
> > > > > > >     return AskOut(
> > > > > > >         answer=FALLBACK_ANSWER, 
> > > > > > >         sources=[], 
> > > > > > >         enough_evidence=False, 
> > > > > > >         run_id=run_id,
> > > > > > >         attempts=attemps, 
> > > > > > >         fallback_used=True
> > > > > > >     )
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:134` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] _record_usage</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/chat_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/chat_service.py:55`
> > > > > > - **역할·로직:** LLMResult의 토큰과 비용을 UsageLog로 저장합니다. 저장 오류는 로그를 남기고 넘깁니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `run_id` | `str` | `필수` | `위치/키워드` | 질문 한 건의 실행 식별자 |
> > > > > > | `result` | `타입 표기 없음` | `필수` | `위치/키워드` | 어댑터가 반환한 LLMResult |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _record_usage(run_id: str, result) -> None:
> > > > > > >     # run_id : 실행 고유번호 
> > > > > > >     # result : 어댑터가 돌려준 LLMResult 타입 응답데이터 
> > > > > > >     try:
> > > > > > >         with session_scope() as session:
> > > > > > >             session.add(
> > > > > > >                 UsageLog(
> > > > > > >                     run_id=run_id, 
> > > > > > >                     model=result.model, 
> > > > > > >                     input_tok=result.input_tok, 
> > > > > > >                     cache_tok=result.cache_tok, 
> > > > > > >                     output_tok=result.output_tok, 
> > > > > > >                     cost_krw=result.cost_krw
> > > > > > >                 )
> > > > > > >             )
> > > > > > >     except Exception as e:
> > > > > > >         log.warning("사용 기록 실패(무시하고 계속): %s", e)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:115` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [독립 함수] ask</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/chat_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/chat_service.py:73`
> > > > > > - **역할·로직:** 질문 검사 → 어댑터 준비 → Run 저장 → trace → 호출·사용량 저장·검증을 최대 3회 → 성공 또는 폴백 → 최종 Run 저장 순서로 처리합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `question` | `str` | `필수` | `키워드 전용` | 사용자 질문 또는 재시도 힌트가 포함된 질문 |
> > > > > > | `run_id` | `str \| None` | `None` | `키워드 전용` | 질문 한 건의 실행 식별자 |
> > > > > > | `user_id` | `int` | `1` | `키워드 전용` | 실행 사용자의 식별자 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `AskOut`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return out
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def ask(*, question: str, run_id: str | None = None, user_id: int = 1) -> AskOut:
> > > > > > >     #1. 가드 호출 -> 여기서 던져진 예외는 이 함수를 통과해 전역 핸들러까지 올라간다. 
> > > > > > >     q = check_question(question) 
> > > > > > >
> > > > > > >     # 2. 어댑터 한 개. 
> > > > > > >     llm = factory.get_llm() 
> > > > > > >
> > > > > > >     # day15 추가 
> > > > > > >     from app.integrations.langfuse_client import score, trace
> > > > > > >     from app.integrations.llm_claude import _extract_json 
> > > > > > >
> > > > > > >     started = time.perf_counter() # 시작시간 
> > > > > > >
> > > > > > >     with session_scope() as session:
> > > > > > >         if run_id is None:
> > > > > > >             run_id = next_run_id(session) # run_id 없으면 생성 
> > > > > > >         session.add(
> > > > > > >             Run(
> > > > > > >                 id=run_id, 
> > > > > > >                 user_id=user_id, 
> > > > > > >                 question=q, 
> > > > > > >                 status="진행중",
> > > > > > >                 mode=get_settings().app_mode
> > > > > > >             )
> > > > > > >         )
> > > > > > >
> > > > > > >     with trace(
> > > > > > >         "ask", 
> > > > > > >         run_id=run_id,
> > > > > > >         user_id=str(user_id),
> > > > > > >         metadata={"question_len" : len(q)},
> > > > > > >     ):
> > > > > > >         out = None
> > > > > > >         hint = ""
> > > > > > >         for attempt in range(1, MAX_ATTEMPTS + 1):
> > > > > > >             # 3. llm 호출 
> > > > > > >             #   프롬프트 준비 
> > > > > > >             prompt = q if not hint else f"{q}\n\n[직전 응답의 문제] {hint}\n출력 형식을 지켜 다시 답해 주세요."
> > > > > > >             #   llm에 질문 던지기 
> > > > > > >             result = llm.answer(question=prompt, contexts=NO_CONTEXTS, user=DEFAULT_USER)
> > > > > > >             
> > > > > > >             # 검증 전에 usage_log 기록 하기 
> > > > > > >             _record_usage(run_id, result)
> > > > > > >
> > > > > > >             try:
> > > > > > >                 data = _extract_json(result.text)
> > > > > > >                 AnswerOut.model_validate(data)   # 규격에 맞는지 검사하는 부분 
> > > > > > >             except ValidationError as e:
> > > > > > >                 hint = _hint_from(e.errors(include_url=False))
> > > > > > >                 # log.warning(f"스키마 위반 {attempt}/{MAX_ATTEMPTS}회 : {hint}")
> > > > > > >                 log.warning("스키마 위반 %d/%d회 : %s", attempt, MAX_ATTEMPTS, hint)
> > > > > > >                 continue 
> > > > > > >
> > > > > > >             # 통과 시 out 변수에 담기 
> > > > > > >             out = AskOut(**data, run_id=run_id, attempts=attempt, fallback_used=False)
> > > > > > >             break 
> > > > > > >         # end of for 
> > > > > > >
> > > > > > >         if out is None:
> > > > > > >             # 3번 다 시도했다. 로그 남기고, 폴백 실행 
> > > > > > >             log.warning("스키마 검증에 %d회 모두 실패하여 폴백으로 응답합니다.(run_id=%s)", MAX_ATTEMPTS, run_id)
> > > > > > >             out = _fallback(run_id, MAX_ATTEMPTS)
> > > > > > >             score(run_id, "schema_ok", 0.0)
> > > > > > >
> > > > > > >         with session_scope() as session:
> > > > > > >             run = session.get(Run, run_id)  # run_id에 해당하는 레코드 한개 조회 
> > > > > > >             run.answer = out.answer
> > > > > > >             run.status = "완료"
> > > > > > >             run.latency_ms = int((time.perf_counter() - started) * 1000)
> > > > > > >             run.sources = [s.model_dump() for s in out.sources]
> > > > > > >
> > > > > > >         return out
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/chat.py:16` — `create_message` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:89` — `test_golden` / 직접 호출
> > > > > > - `FastApi/backend/tests/test_chat_golden.py:97` — `test_golden` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>5. [독립 함수] get_run</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/chat_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/chat_service.py:147`
> > > > > > - **역할·로직:** PK로 실행 기록을 조회해 응답 dict로 변환합니다. 없으면 NotFound입니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `run_id` | `str` | `필수` | `키워드 전용` | 질문 한 건의 실행 식별자 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {'run_id': run_id, 'user_id': run.user_id, 'question': run.question, 'answer': run.answer, 'status': run.status, 'latency_ms': run.latency_ms, 'mode': run.mode, 'sources': run.sources or [], 'created_at': run.created_at.isoformat()}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_run(*, run_id: str) -> dict:
> > > > > > >     with session_scope() as session:
> > > > > > >         run = session.get(Run, run_id) # PK로 레코드 한건 조회 
> > > > > > >         if run is None:
> > > > > > >             raise NotFound(f"실행 기록을 찾을 수 없습니다: {run_id}")
> > > > > > >         return {
> > > > > > >             "run_id": run_id, 
> > > > > > >             "user_id": run.user_id, 
> > > > > > >             "question": run.question,
> > > > > > >             "answer": run.answer, 
> > > > > > >             "status": run.status,
> > > > > > >             "latency_ms":  run.latency_ms, 
> > > > > > >             "mode": run.mode,
> > > > > > >             "sources": run.sources or [], 
> > > > > > >             "created_at": run.created_at.isoformat(),
> > > > > > >         }
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/chat.py:22` — `read_run` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/services/document_service.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `_to_out`, `list_documents`, `get_document`, `create_document`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] _to_out</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/document_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/document_service.py:14`
> > > > > > - **역할·로직:** 문서·문서 버전 ORM 객체를 응답용 dict로 변환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `version` | `DocumentVersion` | `필수` | `위치/키워드` | 문서 버전 문자열 또는 ORM 객체(타입 참고) |
> > > > > > | `document` | `Document` | `필수` | `위치/키워드` | 문서 기본정보 ORM 객체 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {'doc_id': document.id, 'title': document.title, 'dept': document.dept.name, 'version': version.version, 'security_level': document.security_level, 'file_format': version.file_format, 'status': version.status, 'effective_from': version.effective_from, 'expires_at': version.expires_at, 'index_status': version.index_status, 'index_progress': version.index_progress}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def _to_out(version: DocumentVersion, document: Document) -> dict:
> > > > > > >    
> > > > > > >     return {
> > > > > > >         "doc_id": document.id,
> > > > > > >         "title": document.title,
> > > > > > >         "dept": document.dept.name,
> > > > > > >         "version": version.version,
> > > > > > >         "security_level": document.security_level,
> > > > > > >         "file_format": version.file_format,
> > > > > > >         "status": version.status,
> > > > > > >         "effective_from": version.effective_from,
> > > > > > >         "expires_at": version.expires_at,
> > > > > > >         "index_status": version.index_status,
> > > > > > >         "index_progress": version.index_progress,
> > > > > > >     }
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/document_service.py:50` — `list_documents` / 직접 호출
> > > > > > - `FastApi/backend/app/services/document_service.py:62` — `get_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2. [독립 함수] list_documents</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/document_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/document_service.py:31`
> > > > > > - **역할·로직:** DB 세션을 열어 문서 목록을 필터 조건으로 조회하고 응답 dict로 변환합니다. 단건 조회는 현행 버전도 확인합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `dept_id` | `str \| None` | `None` | `키워드 전용` | 부서 식별자 또는 필터 |
> > > > > > | `security_level` | `str \| None` | `None` | `키워드 전용` | 문서 보안 등급 또는 필터 |
> > > > > > | `status` | `str \| None` | `None` | `키워드 전용` | 문서 상태 필터 또는 테스트의 기대 HTTP 상태 코드 |
> > > > > > | `q` | `str \| None` | `None` | `키워드 전용` | 문서 제목·ID 검색어 |
> > > > > > | `limit` | `int` | `50` | `키워드 전용` | 최대 조회 건수 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `list[dict]`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return [_to_out(version, document) for version, document in rows]
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def list_documents(
> > > > > > >     *,
> > > > > > >     dept_id: str | None = None,
> > > > > > >     security_level: str | None = None,
> > > > > > >     status: str | None = None,
> > > > > > >     q: str | None = None,
> > > > > > >     limit: int = 50,
> > > > > > > ) -> list[dict]:
> > > > > > >     
> > > > > > >     with session_scope() as s:
> > > > > > >         rows = document_repo.list_documents(
> > > > > > >             s,
> > > > > > >             dept_id=dept_id,
> > > > > > >             security_level=security_level,
> > > > > > >             status=status,
> > > > > > >             q=q,
> > > > > > >             limit=limit,
> > > > > > >         )
> > > > > > >         
> > > > > > >         return [_to_out(version, document) for version, document in rows]
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:36` — `list_documents` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>3. [독립 함수] get_document</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/document_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/document_service.py:53`
> > > > > > - **역할·로직:** DB 세션을 열어 문서 한 건을 조회하고 응답 dict로 변환합니다. 단건 조회는 현행 버전도 확인합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `doc_id` | `str` | `필수` | `키워드 전용` | 문서 식별자 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return _to_out(current, document)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def get_document(*, doc_id: str) -> dict:
> > > > > > >     
> > > > > > >     with session_scope() as s:
> > > > > > >         document = document_repo.get_document(s, doc_id)
> > > > > > >         if document is None:
> > > > > > >             raise NotFound(f"문서를 찾을 수 없습니다: {doc_id}")
> > > > > > >         current = document.current
> > > > > > >         if current is None:
> > > > > > >             raise NotFound(f"현행 버전이 없습니다: {doc_id}")
> > > > > > >         return _to_out(current, document)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:88` — `get_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>4. [독립 함수] create_document</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/document_service.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/document_service.py:65`
> > > > > > - **역할·로직:** 문서가 없으면 생성하고, 같은 버전 중복을 거절한 뒤 새 버전을 추가합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `doc_id` | `str` | `필수` | `키워드 전용` | 문서 식별자 |
> > > > > > | `title` | `str` | `필수` | `키워드 전용` | 제목 |
> > > > > > | `dept_id` | `str` | `필수` | `키워드 전용` | 부서 식별자 또는 필터 |
> > > > > > | `security_level` | `str` | `필수` | `키워드 전용` | 문서 보안 등급 또는 필터 |
> > > > > > | `version` | `str` | `필수` | `키워드 전용` | 문서 버전 문자열 또는 ORM 객체(타입 참고) |
> > > > > > | `effective_from` | `date` | `필수` | `키워드 전용` | 문서 시행일 |
> > > > > > | `file_path` | `str` | `필수` | `키워드 전용` | 저장된 문서 파일 경로 |
> > > > > > | `file_format` | `str` | `필수` | `키워드 전용` | 문서 파일 형식 |
> > > > > > | `owner_id` | `int \| None` | `None` | `키워드 전용` | 문서 소유자 식별자 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `dict`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return {'doc_id': document.id, 'title': document.title, 'version': version, 'file_format': file_format, 'file_path': file_path, 'created': created}
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def create_document(
> > > > > > >     *,
> > > > > > >     doc_id: str,
> > > > > > >     title: str,
> > > > > > >     dept_id: str,
> > > > > > >     security_level: str,
> > > > > > >     version: str,
> > > > > > >     effective_from: date,
> > > > > > >     file_path: str,
> > > > > > >     file_format: str,
> > > > > > >     owner_id: int | None = None,
> > > > > > > ) -> dict:
> > > > > > >
> > > > > > >     with session_scope() as s:
> > > > > > >         document = document_repo.get_document(s, doc_id)
> > > > > > >         created = document is None
> > > > > > >         if document is None:
> > > > > > >             document = Document(
> > > > > > >                 id=doc_id,
> > > > > > >                 title=title,
> > > > > > >                 dept_id=dept_id,
> > > > > > >                 security_level=security_level,
> > > > > > >                 owner_id=owner_id,
> > > > > > >             )
> > > > > > >             s.add(document)
> > > > > > >             s.flush()
> > > > > > >         elif any(v.version == version for v in document.versions):
> > > > > > >             raise ValidationFailed(
> > > > > > >                 f"{doc_id} 의 {version} 은(는) 이미 등록되어 있습니다. "
> > > > > > >                 "판 번호를 올려 다시 올려 주세요."
> > > > > > >             )
> > > > > > >
> > > > > > >         document_repo.add_version(
> > > > > > >             s,
> > > > > > >             document,
> > > > > > >             version=version,
> > > > > > >             status="현행",
> > > > > > >             effective_from=effective_from,
> > > > > > >             expires_at=None,
> > > > > > >             file_path=file_path,
> > > > > > >             file_format=file_format,
> > > > > > >             index_status="대기",     
> > > > > > >         )
> > > > > > >         return {
> > > > > > >             "doc_id": document.id,
> > > > > > >             "title": document.title,
> > > > > > >             "version": version,
> > > > > > >             "file_format": file_format,
> > > > > > >             "file_path": file_path,
> > > > > > >             "created": created,
> > > > > > >         }
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/api/v1/documents.py:74` — `upload_document` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/app/services/ids.py</h1></summary>
> > > > >
> > > > > **파일 구성**
> > > > >
> > > > > - 클래스: 없음
> > > > > - 파일 수준 함수: `next_run_id`
> > > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > > >
> > > > >
> > > > > <details>
> > > > > <summary><h2>1. [독립 함수] next_run_id</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/app/services/ids.py`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/app/services/ids.py:10`
> > > > > > - **역할·로직:** 기존 RUN-숫자 중 최댓값에 1을 더해 다음 실행 번호를 만듭니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `session` | `Session` | `필수` | `위치/키워드` | DB 작업용 SQLAlchemy 세션 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `str`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return f'RUN-{max(numbers) + 1:04d}'
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def next_run_id(session: Session) -> str:
> > > > > > >     # DB에서 조회 
> > > > > > >     used = session.scalars(select(Run.id)).all() 
> > > > > > >
> > > > > > >     numbers = [RUN_START - 1]    # 아무 행도 없을때 max() 가 죽지 않도록 하는 바닥값 
> > > > > > >     for run_id in used:
> > > > > > >         tail = run_id.removeprefix("RUN-")
> > > > > > >         if tail.isdigit():
> > > > > > >             numbers.append(int(tail))
> > > > > > >
> > > > > > >     return f"RUN-{max(numbers) + 1:04d}"
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/backend/app/services/chat_service.py:15` — `모듈 import` / import/재공개
> > > > > > - `FastApi/backend/app/services/chat_service.py:88` — `ask` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/backend/tests</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/conftest.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `travel_doc`, `client`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] travel_doc</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/conftest.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/conftest.py:8`
> > > > > - **역할·로직:** 예외 테스트에서 사용하는 문서 샘플 dict를 제공합니다.
> > > > > - **데코레이터:** `pytest.fixture`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return {'doc_id': 'DOC-HR-014', 'title': '국내출장 여비 규정', 'dept': '인사', 'version': 'v2.0', 'security_level': '일반', 'file_format': 'docx', 'status': '현행'}
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def travel_doc() -> dict:
> > > > > >     return {
> > > > > >         "doc_id": "DOC-HR-014",
> > > > > >         "title": "국내출장 여비 규정",
> > > > > >         "dept": "인사",
> > > > > >         "version": "v2.0",
> > > > > >         "security_level": "일반",
> > > > > >         "file_format": "docx",
> > > > > >         "status": "현행",
> > > > > >     }
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastApi/backend/tests/test_exceptions.py의 test_detail_is_optional_and_kept에 pytest가 주입합니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] client</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/conftest.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/conftest.py:21`
> > > > > - **역할·로직:** FastAPI TestClient를 with로 열어 테스트에 제공하고 정리합니다.
> > > > > - **데코레이터:** `pytest.fixture`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `타입 표기 없음`
> > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > - 호출하면 제너레이터를 반환합니다. pytest/FastAPI 등이 순회하며 아래 값을 받아 사용합니다.
> > > > > - 제공 값: `(yield c)`
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def client():
> > > > > >     with TestClient(app) as c:
> > > > > >         yield c
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - FastApi/backend/tests/test_health.py의 client 매개변수를 가진 테스트에 pytest가 주입합니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_chat_golden.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: `StubLLM`
> > > > - 파일 수준 함수: `check`, `_question_of`, `test_golden`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [클래스] StubLLM</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:18`
> > > > > - **역할·로직:** 미리 넣은 응답을 호출 순서대로 반환하는 테스트용 어댑터입니다.
> > > > > - **상속:** 명시적 부모 없음(object)
> > > > > - **클래스 호출 결과:** `StubLLM` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > - **직접 정의한 메서드:** `__init__`, `answer`
> > > > > - **생성 매개변수:** 아래 `StubLLM.__init__`의 self를 제외한 매개변수.
> > > > >
> > > > > **필드·클래스 속성 선언**
> > > > >
> > > > > ```python
> > > > > name = 'stub'
> > > > > ```
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_chat_golden.py:23` — `StubLLM.__init__` / 참조·타입·콜백 등
> > > > > - `FastApi/backend/tests/test_chat_golden.py:24` — `StubLLM.__init__` / 참조·타입·콜백 등
> > > > > - `FastApi/backend/tests/test_chat_golden.py:27` — `StubLLM.answer` / 참조·타입·콜백 등
> > > > > - `FastApi/backend/tests/test_chat_golden.py:28` — `StubLLM.answer` / 참조·타입·콜백 등
> > > > > - `FastApi/backend/tests/test_chat_golden.py:94` — `test_golden` / 직접 호출
> > > > >
> > > > > **이 클래스의 메서드**
> > > > >
> > > > > - 1.1 `StubLLM.__init__`
> > > > > - 1.2 `StubLLM.answer`
> > > > >
> > > > > <details>
> > > > > <summary><h2>1.1. [초기화 메서드] StubLLM.__init__</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > > >
> > > > > > **소속 클래스:** `StubLLM`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:22`
> > > > > > - **역할·로직:** 응답 목록을 복사하고 호출 횟수를 0으로 초기화합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > | `replies` | `list[str]` | `필수` | `위치/키워드` | 호출 순서대로 반환할 가짜 응답 목록 |
> > > > > >
> > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `None`
> > > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def __init__(self, replies: list[str]) -> None:
> > > > > > >         self.replies = list(replies)
> > > > > > >         self.calls = 0
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **자동 호출·사용 방식**
> > > > > >
> > > > > > - 이 클래스의 객체 생성 시 자동 호출됩니다. 호출·사용 위치는 위 클래스 항목에도 나열합니다. self는 파이썬이 자동 전달합니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > >
> > > > > > - `FastApi/backend/app/core/exceptions.py:7` — `AgentError.__init__` / 대상 확인 필요: super().__init__
> > > > > > - `FastApi/backend/app/core/exceptions.py:59` — `AuthFailed.__int__` / 대상 확인 필요: super().__init__
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>1.2. [인스턴스 메서드] StubLLM.answer</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > > >
> > > > > > **소속 클래스:** `StubLLM`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:26`
> > > > > > - **역할·로직:** 현재 호출 순서의 응답을 선택하고 횟수를 증가시켜 LLMResult로 반환합니다. 목록을 소진하면 마지막 응답을 재사용합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `self` | `타입 표기 없음` | `필수` | `위치/키워드` | 현재 객체; 인스턴스 메서드에 자동 전달 |
> > > > > > | `question` | `str` | `필수` | `키워드 전용` | 사용자 질문 또는 재시도 힌트가 포함된 질문 |
> > > > > > | `contexts` | `list[dict]` | `필수` | `키워드 전용` | 모델에게 전달할 근거 문서 dict 목록 |
> > > > > > | `user` | `dict` | `필수` | `키워드 전용` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > > >
> > > > > > `self`는 현재 객체이며 인스턴스 메서드 호출 시 자동 전달됩니다.
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `LLMResult`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return LLMResult(text=text, model='claude-haiku-4-5', input_tok=1200, output_tok=300, cost_krw=2.3, latency_ms=900)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def answer(self, *, question: str, contexts: list[dict], user: dict) -> LLMResult:
> > > > > > >         text = self.replies[min(self.calls, len(self.replies) - 1)]
> > > > > > >         self.calls += 1
> > > > > > >
> > > > > > >         return LLMResult(
> > > > > > >             text=text,
> > > > > > >             model="claude-haiku-4-5",
> > > > > > >             input_tok=1200,
> > > > > > >             output_tok=300,
> > > > > > >             cost_krw=2.3,
> > > > > > >             latency_ms=900,
> > > > > > >         )
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **자동 호출·사용 방식**
> > > > > >
> > > > > > - FastApi/backend/app/services/chat_service.py의 ask가 llm.answer(...)로 호출합니다. live에서는 FastApi/backend/app/integrations/factory.py가 반환한 ClaudeLLM.answer, 골든셋에서는 FastApi/backend/tests/test_chat_golden.py의 StubLLM.answer가 실행됩니다. LLMPort.answer 본문이 대신 실행되는 구조는 아닙니다. FastApi/backend/app/agent/chain.py의 call_port에도 같은 포트 호출이 있습니다.
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > > >
> > > > > > **동적 메서드·속성 참조 후보 — 실제 대상은 위 설명과 객체 생성 경로로 확인**
> > > > > >
> > > > > > - `FastApi/backend/app/agent/chain.py:59` — `build_result_chain.call_port` / 대상 확인 필요: llm.answer
> > > > > > - `FastApi/backend/app/services/chat_service.py:112` — `ask` / 대상 확인 필요: llm.answer
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] check</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:40`
> > > > > - **역할·로직:** 최종 응답의 포함·제외 문구, 출처 수·문서 ID, 시도 횟수와 플래그를 기대 조건과 비교해 문제 목록을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `case` | `dict` | `필수` | `위치/키워드` | 골든셋 사례 한 건 |
> > > > > | `out` | `타입 표기 없음` | `필수` | `위치/키워드` | 서비스가 반환한 최종 응답 객체 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `list[str]`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return problems
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def check(case: dict, out) -> list[str]:
> > > > > >     expect = case["expect"]
> > > > > >     problems: list[str] = []
> > > > > >
> > > > > >
> > > > > >     for needle in expect.get("contains", []):
> > > > > >         if needle not in out.answer:
> > > > > >             problems.append(f"answer 에 '{needle}' 이 없습니다")
> > > > > >
> > > > > >
> > > > > >     for needle in expect.get("not_contains", []):
> > > > > >         if needle in out.answer:
> > > > > >             problems.append(f"answer 에 '{needle}' 이 들어 있습니다")
> > > > > >
> > > > > >     if "min_sources" in expect and len(out.sources) < expect["min_sources"]:
> > > > > >         problems.append(
> > > > > >             f"근거가 {expect['min_sources']}건 이상이어야 합니다 (현재 {len(out.sources)}건)"
> > > > > >         )
> > > > > >     if "max_sources" in expect and len(out.sources) > expect["max_sources"]:
> > > > > >         problems.append(
> > > > > >             f"sources 가 {expect['max_sources']}건이어야 합니다 (현재 {len(out.sources)}건)"
> > > > > >         )
> > > > > >     for key in ("attempts", "fallback_used", "enough_evidence"):
> > > > > >         if key in expect and getattr(out, key) != expect[key]:
> > > > > >             problems.append(f"{key} 가 {expect[key]} 여야 합니다")
> > > > > >
> > > > > >     if "doc_ids" in expect:
> > > > > >         for source in out.sources:
> > > > > >             if source.doc_id not in expect["doc_ids"]:
> > > > > >                 problems.append(f"허용되지 않은 doc_id: {source.doc_id}")
> > > > > >
> > > > > >     return problems
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_chat_golden.py:100` — `test_golden` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] _question_of</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:74`
> > > > > - **역할·로직:** 사례의 question을 repeat 횟수만큼 반복해 실제 테스트 질문을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `case` | `dict` | `필수` | `위치/키워드` | 골든셋 사례 한 건 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return case['question'] * case.get('repeat', 1)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _question_of(case: dict) -> str:
> > > > > >     return case["question"] * case.get("repeat", 1)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_chat_golden.py:89` — `test_golden` / 직접 호출
> > > > > - `FastApi/backend/tests/test_chat_golden.py:97` — `test_golden` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] test_golden</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_chat_golden.py:79`
> > > > > - **역할·로직:** 사례별로 가드 예외를 검사하거나 StubLLM을 주입해 서비스 결과가 기대 규칙을 만족하는지 검사합니다.
> > > > > - **데코레이터:** `pytest.mark.parametrize('case', GOLDEN, ids=[c['id'] for c in GOLDEN])`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `case` | `dict` | `필수` | `위치/키워드` | 골든셋 사례 한 건 |
> > > > > | `monkeypatch` | `타입 표기 없음` | `필수` | `위치/키워드` | pytest의 임시 속성 교체 도구 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_golden(case: dict, monkeypatch) -> None:
> > > > > >     
> > > > > >     expect = case["expect"]
> > > > > >
> > > > > >    
> > > > > >     if "raises" in expect:
> > > > > >         with pytest.raises(GuardTripped) as caught:
> > > > > >             if case.get("guard") == "check_model":
> > > > > >                 check_model(case["question"])
> > > > > >             else:
> > > > > >                 chat_service.ask(question=_question_of(case))
> > > > > >         for needle in expect.get("contains", []):
> > > > > >             assert needle in str(caught.value)
> > > > > >         return
> > > > > >
> > > > > >     stub = StubLLM(case["stub"])
> > > > > >     monkeypatch.setattr(factory, "get_llm", lambda: stub)
> > > > > >
> > > > > >     out = chat_service.ask(question=_question_of(case))
> > > > > >
> > > > > >     assert stub.calls > 0, "가짜 어댑터가 한 번도 불리지 않았습니다"
> > > > > >     assert check(case, out) == []
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > > **이 함수 안의 함수**
> > > > >
> > > > > - 4.1 `lambda 1`
> > > > >
> > > > > <details>
> > > > > <summary><h2>4.1. [익명 함수] lambda 1</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/backend/tests/test_chat_golden.py`
> > > > > >
> > > > > > **소속 함수:** `test_golden`
> > > > > >
> > > > > > - **파일:** `FastApi/backend/tests/test_chat_golden.py:95`
> > > > > >   - 매개변수: ``
> > > > > >   - 반환: `stub`
> > > > > >   - 로직: 표현식을 계산해 그대로 반환합니다.
> > > > > >   - 사용 위치: `FastApi/backend/tests/test_chat_golden.py`의 `test_golden`에서 `monkeypatch.setattr(factory, 'get_llm', lambda: stub)`에 전달됩니다.
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_core_config.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `test_get_settings_returns_same_instance`, `test_settings_has_defaults`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] test_get_settings_returns_same_instance</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_core_config.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_core_config.py:3`
> > > > > - **역할·로직:** 설정 객체 캐시 재사용를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_get_settings_returns_same_instance() -> None:
> > > > > >     assert get_settings() is get_settings()
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] test_settings_has_defaults</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_core_config.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_core_config.py:6`
> > > > > - **역할·로직:** 설정 기본값를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_settings_has_defaults() -> None:
> > > > > >     settings = get_settings()
> > > > > >     assert settings.app_mode == "mock"
> > > > > >     assert settings.debug is False
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_exceptions.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `test_domain_exception_maps_to_status_and_code`, `test_every_domain_exception_is_agent_error`, `test_detail_is_optional_and_kept`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] test_domain_exception_maps_to_status_and_code</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_exceptions.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_exceptions.py:22`
> > > > > - **역할·로직:** 예외별 상태 코드와 오류 코드를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > > - **데코레이터:** `pytest.mark.parametrize('exc_cls,status,code', CASES)`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `exc_cls` | `타입 표기 없음` | `필수` | `위치/키워드` | 테스트할 예외 클래스 |
> > > > > | `status` | `타입 표기 없음` | `필수` | `위치/키워드` | 문서 상태 필터 또는 테스트의 기대 HTTP 상태 코드 |
> > > > > | `code` | `타입 표기 없음` | `필수` | `위치/키워드` | 기대 오류 코드 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_domain_exception_maps_to_status_and_code(exc_cls, status, code) -> None:
> > > > > >     exc = exc_cls("문서를 찾을 수 없습니다: DOC-HR-014")
> > > > > >     assert exc.status_code == status
> > > > > >     assert exc.code == code
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] test_every_domain_exception_is_agent_error</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_exceptions.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_exceptions.py:28`
> > > > > - **역할·로직:** 프로젝트 예외들의 AgentError 상속를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_every_domain_exception_is_agent_error() -> None:
> > > > > >     for exc_cls, _status, _code in CASES:
> > > > > >         assert issubclass(exc_cls, AgentError)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] test_detail_is_optional_and_kept</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_exceptions.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_exceptions.py:33`
> > > > > - **역할·로직:** 예외의 선택적 detail과 message 저장를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `travel_doc` | `타입 표기 없음` | `필수` | `위치/키워드` | fixture가 제공하는 문서 샘플 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_detail_is_optional_and_kept(travel_doc) -> None:
> > > > > >     없음 = NotFound(f"문서를 찾을 수 없습니다: {travel_doc['doc_id']}")
> > > > > >     assert 없음.detail is None
> > > > > >     assert 없음.message == "문서를 찾을 수 없습니다: DOC-HR-014"
> > > > > >
> > > > > >     있음 = NotFound("문서를 찾을 수 없습니다: DOC-HR-014", detail="인사팀 시드 데이터 누락")
> > > > > >     assert 있음.detail == "인사팀 시드 데이터 누락"
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_guards.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `test_check_question_passed_and_strips`, `test_check_question_rejects_blank`, `test_check_question_rejects_too_long`, `test_check_model_rejects_unknown_model`, `test_check_daily_limit_raises_when_exhausted`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] test_check_question_passed_and_strips</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_guards.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_guards.py:8`
> > > > > - **역할·로직:** 정상 질문 통과와 앞뒤 공백 제거를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_check_question_passed_and_strips() -> None:
> > > > > >     assert check_question("  제주도 출장 숙박비 한도가 얼마인가요?  ") == "제주도 출장 숙박비 한도가 얼마인가요?"
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] test_check_question_rejects_blank</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_guards.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_guards.py:11`
> > > > > - **역할·로직:** 빈 질문 거절를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_check_question_rejects_blank() -> None:
> > > > > >     with pytest.raises(GuardTripped):
> > > > > >         check_question("   ")
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] test_check_question_rejects_too_long</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_guards.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_guards.py:15`
> > > > > - **역할·로직:** 최대 길이 초과 거절를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_check_question_rejects_too_long() -> None:
> > > > > >     limit = get_settings().max_input_chars
> > > > > >     with pytest.raises(GuardTripped):
> > > > > >         check_question("가" * (limit + 1))
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] test_check_model_rejects_unknown_model</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_guards.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_guards.py:20`
> > > > > - **역할·로직:** 미허용 모델 거절과 설정 모델 통과를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_check_model_rejects_unknown_model() -> None:
> > > > > >     with pytest.raises(GuardTripped):
> > > > > >         check_model("claude-opus-5")
> > > > > >     assert check_model(get_settings().llm_model) == get_settings().llm_model
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] test_check_daily_limit_raises_when_exhausted</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_guards.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_guards.py:25`
> > > > > - **역할·로직:** 한도 직전 통과와 한도 도달 거절를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_check_daily_limit_raises_when_exhausted() -> None:
> > > > > >     limit = get_settings().daily_call_limit
> > > > > >     check_daily_limit(limit - 1)
> > > > > >     with pytest.raises(RateLimited):
> > > > > >         check_daily_limit(limit)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_health.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `test_health_returns_ok`, `test_documents_list_returns_rows`, `test_unknown_document_returns_404_with_code`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] test_health_returns_ok</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_health.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_health.py:2`
> > > > > - **역할·로직:** health API의 200과 status=ok를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `client` | `타입 표기 없음` | `필수` | `위치/키워드` | pytest가 주입한 FastAPI TestClient |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_health_returns_ok(client) -> None:
> > > > > >     """GET /health 는 200 과 {"status":"ok"} 를 돌려준다."""
> > > > > >     r = client.get("/health")
> > > > > >     assert r.status_code == 200
> > > > > >     assert r.json() == {"status": "ok"}
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] test_documents_list_returns_rows</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_health.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_health.py:9`
> > > > > - **역할·로직:** 문서 목록 응답과 secret_note 제외를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `client` | `타입 표기 없음` | `필수` | `위치/키워드` | pytest가 주입한 FastAPI TestClient |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_documents_list_returns_rows(client) -> None:
> > > > > >     r = client.get("/api/v1/documents")
> > > > > >     assert r.status_code == 200
> > > > > >     문서들 = r.json()
> > > > > >     assert len(문서들) > 0
> > > > > >     assert 문서들[0]["security_level"] in ("일반", "3급", "대외비")
> > > > > >     # secret_note 는 응답 모델에 없으므로 밖으로 나가면 안 된다.
> > > > > >     assert "secret_note" not in 문서들[0]
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] test_unknown_document_returns_404_with_code</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_health.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_health.py:19`
> > > > > - **역할·로직:** 없는 문서의 404와 오류 코드를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `client` | `타입 표기 없음` | `필수` | `위치/키워드` | pytest가 주입한 FastAPI TestClient |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_unknown_document_returns_404_with_code(client) -> None:
> > > > > >     r = client.get("/api/v1/documents/DOC-HR-999")
> > > > > >     assert r.status_code == 404
> > > > > >     본문 = r.json()
> > > > > >     assert 본문["code"] == "not_found"
> > > > > >     assert "DOC-HR-999" in 본문["message"]
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/backend/tests/test_layers.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `_top_level_imports`, `_py_files`, `_is`, `_violations`, `test_models_import_nothing_but_models`, `test_api_does_not_import_repositories_or_models`, `test_services_do_not_import_api`, `test_repositories_do_not_import_services_or_api`, `test_services_reach_integrations_only_through_factory`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] _top_level_imports</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:16`
> > > > > - **역할·로직:** 파이썬 파일을 AST로 읽어 모듈 최상단의 import 이름만 모읍니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `path` | `Path` | `필수` | `위치/키워드` | 읽을 파일 경로 또는 HTTP 경로(함수 역할 참고) |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `list[str]`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return names
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _top_level_imports(path: Path) -> list[str]:
> > > > > >
> > > > > >     tree = ast.parse(path.read_text(encoding="utf-8"))
> > > > > >     names: list[str] = []
> > > > > >     for node in tree.body:
> > > > > >         if isinstance(node, ast.Import):
> > > > > >             names += [alias.name for alias in node.names]
> > > > > >         elif isinstance(node, ast.ImportFrom):
> > > > > >             if node.module:
> > > > > >                 names.append(node.module)
> > > > > >     return names
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_layers.py:51` — `_violations` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] _py_files</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:30`
> > > > > - **역할·로직:** 지정 계층 폴더 아래의 파이썬 파일 경로를 정렬해 반환합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `layer` | `str` | `필수` | `위치/키워드` | 검사할 계층 폴더 이름 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `list[Path]`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return []
> > > > > return sorted(folder.rglob('*.py'))
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _py_files(layer: str) -> list[Path]:
> > > > > >
> > > > > >     folder = APP / layer
> > > > > >     if not folder.is_dir():
> > > > > >         return []
> > > > > >     return sorted(folder.rglob("*.py"))
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_layers.py:50` — `_violations` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] _is</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:39`
> > > > > - **역할·로직:** 모듈 이름이 지정 패키지 또는 그 하위 모듈인지 판단합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `name` | `str` | `필수` | `위치/키워드` | 프롬프트·로그·trace·점수 등의 이름(함수 역할 참고) |
> > > > > | `prefix` | `str` | `필수` | `위치/키워드` | 비교할 모듈 접두어 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `bool`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return name == prefix or name.startswith(prefix + '.')
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _is(name: str, prefix: str) -> bool:
> > > > > >     return name == prefix or name.startswith(prefix + ".")
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_layers.py:52` — `_violations` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:54` — `_violations` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:56` — `_violations` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] _violations</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:44`
> > > > > - **역할·로직:** 계층 파일의 import 중 허용 예외를 제외하고 금지된 참조 목록을 수집합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `layer` | `str` | `필수` | `위치/키워드` | 검사할 계층 폴더 이름 |
> > > > > | `forbidden` | `tuple[str, ...]` | `필수` | `위치/키워드` | 금지할 import 접두어 목록 |
> > > > > | `allowed` | `tuple[str, ...]` | `()` | `위치/키워드` | 허용할 import 접두어 목록 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `list[str]`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return found
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _violations(
> > > > > >     layer: str,
> > > > > >     forbidden: tuple[str, ...],
> > > > > >     allowed: tuple[str, ...] = (),
> > > > > > ) -> list[str]:
> > > > > >     found: list[str] = []
> > > > > >     for path in _py_files(layer):
> > > > > >         for name in _top_level_imports(path):
> > > > > >             if not _is(name, OURS):
> > > > > >                 continue  # 외부 패키지는 관심 밖
> > > > > >             if any(_is(name, ok) for ok in allowed):
> > > > > >                 continue
> > > > > >             if any(_is(name, bad) for bad in forbidden):
> > > > > >                 found.append(f"{path.relative_to(APP)} → {name}")
> > > > > >     return found
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/backend/tests/test_layers.py:63` — `test_models_import_nothing_but_models` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:73` — `test_api_does_not_import_repositories_or_models` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:82` — `test_services_do_not_import_api` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:91` — `test_repositories_do_not_import_services_or_api` / 직접 호출
> > > > > - `FastApi/backend/tests/test_layers.py:100` — `test_services_reach_integrations_only_through_factory` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] test_models_import_nothing_but_models</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:62`
> > > > > - **역할·로직:** 모델 계층의 역방향 import 금지를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_models_import_nothing_but_models() -> None:
> > > > > >     offenders = _violations("models", forbidden=(OURS,), allowed=("app.models",))
> > > > > >     assert not offenders, (
> > > > > >         "models 가 다른 계층을 import 합니다. 모델은 맨 아래층이라 아무도 올려다보지 "
> > > > > >         "않습니다. 필요한 값은 인자로 받고, 규칙은 services 로 올리세요:\n  "
> > > > > >         + "\n  ".join(offenders)
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>6. [독립 함수] test_api_does_not_import_repositories_or_models</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:72`
> > > > > - **역할·로직:** API의 repository/model 직접 import 금지를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_api_does_not_import_repositories_or_models() -> None:
> > > > > >     offenders = _violations("api/v1", forbidden=("app.repositories", "app.models"))
> > > > > >     assert not offenders, (
> > > > > >         "라우터가 repositories/models 를 직접 import 합니다. 그 호출을 services 의 "
> > > > > >         "함수로 옮기고 라우터는 그 함수만 부르세요:\n  " + "\n  ".join(offenders)
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>7. [독립 함수] test_services_do_not_import_api</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:81`
> > > > > - **역할·로직:** 서비스의 API import 금지를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_services_do_not_import_api() -> None:
> > > > > >     offenders = _violations("services", forbidden=("app.api",))
> > > > > >     assert not offenders, (
> > > > > >         "services 가 api 를 import 합니다. 의존이 거꾸로 섰습니다. 필요한 값은 "
> > > > > >         "라우터가 인자로 내려 주게 바꾸세요:\n  " + "\n  ".join(offenders)
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>8. [독립 함수] test_repositories_do_not_import_services_or_api</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:90`
> > > > > - **역할·로직:** 리포지토리의 서비스/API import 금지를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_repositories_do_not_import_services_or_api() -> None:
> > > > > >     offenders = _violations("repositories", forbidden=("app.services", "app.api"))
> > > > > >     assert not offenders, (
> > > > > >         "repositories 가 services/api 를 import 합니다. 판단은 services 에 두고 "
> > > > > >         "리포지토리는 값만 돌려주세요:\n  " + "\n  ".join(offenders)
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>9. [독립 함수] test_services_reach_integrations_only_through_factory</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/backend/tests/test_layers.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/backend/tests/test_layers.py:99`
> > > > > - **역할·로직:** 서비스 최상단 import가 integrations의 factory만 참조하는지를 assert 또는 pytest.raises로 검사합니다. 실패하면 테스트 오류입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def test_services_reach_integrations_only_through_factory() -> None:
> > > > > >     offenders = _violations(
> > > > > >         "services",
> > > > > >         forbidden=("app.integrations",),
> > > > > >         allowed=("app.integrations.factory",),
> > > > > >     )
> > > > > >     assert not offenders, (
> > > > > >         "services 가 어댑터를 직접 import 합니다. integrations/factory.py 를 거쳐 "
> > > > > >         "Protocol 타입으로만 받으세요:\n  " + "\n  ".join(offenders)
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **자동 호출·사용 방식**
> > > > >
> > > > > - pytest가 이 파일을 수집해 호출합니다. 매개변수는 fixture 또는 parametrize 값으로 주입됩니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[폴더] FastApi/backend/tests/golden</h1></summary>
> > > >
> > > > <details>
> > > > <summary><h1>[파일] FastApi/backend/tests/golden/chat_golden.json</h1></summary>
> > > > >
> > > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > > - **사용 위치:** FastApi/backend/tests/test_chat_golden.py의 모듈 실행부가 읽고 test_golden의 매개변수 사례로 사용합니다.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > </details>
> >
> </details>
>
> <details>
> <summary><h1>[폴더] FastApi/frontend</h1></summary>
> >
> > <details>
> > <summary><h1>[파일] FastApi/frontend/app.py</h1></summary>
> > >
> > > **파일 구성**
> > >
> > > - 클래스: 없음
> > > - 파일 수준 함수: `render_sidebar`, `main`
> > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > >
> > >
> > > <details>
> > > <summary><h2>1. [독립 함수] render_sidebar</h2></summary>
> > > >
> > > > **소속 파일:** `FastApi/frontend/app.py`
> > > >
> > > > - **정의 파일:** `FastApi/frontend/app.py:33`
> > > > - **역할·로직:** 로그인 사용자 정보, 로그아웃 버튼, 메뉴를 사이드바에 그립니다.
> > > >
> > > > **매개변수**
> > > >
> > > > 없음.
> > > >
> > > > **반환값**
> > > >
> > > > - 선언: `None`
> > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > >
> > > > <details>
> > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > >
> > > > > ```python
> > > > > def render_sidebar() -> None:
> > > > >     st.sidebar.markdown(
> > > > >         '<div class="ag-brand"><div class="ag-brand-name">사내 업무 에이전트</div></div>',
> > > > >         unsafe_allow_html=True,
> > > > >     )
> > > > >
> > > > >     # 추가 
> > > > >     user = session.current_user() # 회원정보 조회, 비로그인시 None
> > > > >     # 로그인 했으면 
> > > > >     if user is not None:
> > > > >         # 사용자 이름과 부서명을 화면에 그리기 
> > > > >         st.sidebar.markdown(
> > > > >             '<div class="ag-user"><div>'
> > > > >             f'<div class="ag-user-name">{html.escape(user["name"])}</div>'
> > > > >             f'<div class="ag-user-role">{html.escape(user["dept"])}</div>'
> > > > >             '</div></div>',
> > > > >             unsafe_allow_html=True,
> > > > >         )
> > > > >         # 로그아웃 버튼 부착 : 버튼 누르면 로그아웃 처리 
> > > > >         if st.sidebar.button("로그아웃", key="nav_logout"):
> > > > >             session.logout()
> > > > >             st.rerun()      
> > > > >
> > > > >     # 메뉴 버튼 그리기 
> > > > >     for label, page_key in NAV:
> > > > >         if st.sidebar.button(label, key=f"nav_{label}"):
> > > > >             if page_key is None:
> > > > >                 st.sidebar.info("아직 만들지 않은 화면입니다.")
> > > > >             else:
> > > > >                 # 메뉴 누르면 화면 키값을 상태에 추가 -> 화면 이동 처리 
> > > > >                 st.session_state["page"] = page_key
> > > > > ```
> > > > >
> > > > </details>
> > > >
> > > > **호출·사용 위치**
> > > >
> > > > - `FastApi/frontend/app.py:76` — `main` / 직접 호출
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h2>2. [독립 함수] main</h2></summary>
> > > >
> > > > **소속 파일:** `FastApi/frontend/app.py`
> > > >
> > > > - **정의 파일:** `FastApi/frontend/app.py:66`
> > > > - **역할·로직:** 세션을 초기화하고 로그인 여부에 따라 로그인 화면 또는 사이드바·문서 화면을 그립니다.
> > > >
> > > > **매개변수**
> > > >
> > > > 없음.
> > > >
> > > > **반환값**
> > > >
> > > > - 선언: `None`
> > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > >
> > > > <details>
> > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > >
> > > > > ```python
> > > > > def main() -> None:
> > > > >     # 상태값 초기화 
> > > > >     session.init_state()
> > > > >
> > > > >     # 로그인 상태 확인 
> > > > >     if not session.is_authenticated():  # 비 로그인이면, 
> > > > >         login_view.render()  # 로그인 화면 보여주기 
> > > > >         return 
> > > > >
> > > > >     # 사이드바 그리기 
> > > > >     render_sidebar()
> > > > >
> > > > >     # 현재 페이지 키 가져오기 
> > > > >     page = router.current_page()
> > > > >     # 현재 페이지 키값이 documents 
> > > > >     if page == "documents":
> > > > >         documents_view.render()
> > > > >     else:
> > > > >         st.info("아직 만들지 않은 화면입니다.")
> > > > > ```
> > > > >
> > > > </details>
> > > >
> > > > **호출·사용 위치**
> > > >
> > > > - `FastApi/frontend/app.py:87` — `모듈 실행부` / 직접 호출
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[파일] FastApi/frontend/ui_kit_demo.py</h1></summary>
> > >
> > > 직접 정의한 함수·클래스: **없음**.
> > >
> > > Streamlit 실행 시 모듈 실행부에서 공통 UI 함수를 호출해 예시 화면을 그립니다. 각 UI 함수의 사용 위치에 이 파일이 표시됩니다.
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/frontend/.streamlit</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/.streamlit/config.toml</h1></summary>
> > > >
> > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > - **사용 위치:** Streamlit이 프런트엔드 실행 시 읽는 설정입니다.
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/frontend/assets</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/assets/base.css</h1></summary>
> > > >
> > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > - **사용 위치:** FastApi/frontend/ui/theme.py의 load_css가 읽고 inject_css가 화면에 적용합니다. CSS 선택자·스타일 선언이며 Python 클래스는 아닙니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/assets/components.css</h1></summary>
> > > >
> > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > - **사용 위치:** FastApi/frontend/ui/theme.py의 load_css가 읽고 inject_css가 화면에 적용합니다. CSS 선택자·스타일 선언이며 Python 클래스는 아닙니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/assets/tokens.css</h1></summary>
> > > >
> > > > - **함수·클래스:** 설정 또는 데이터 파일이며 Python 함수·클래스 정의는 없습니다.
> > > > - **사용 위치:** FastApi/frontend/ui/theme.py의 load_css가 읽고 inject_css가 화면에 적용합니다. CSS 선택자·스타일 선언이며 Python 클래스는 아닙니다.
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/frontend/core</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/core/__init__.py</h1></summary>
> > > >
> > > > 직접 정의한 함수·클래스: **없음**.
> > > >
> > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/core/api_client.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: `ApiError`
> > > > - 파일 수준 함수: `_request`, `login`, `me`, `list_documents`, `get_document`, `stats`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [클래스] ApiError</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:12`
> > > > > - **역할·로직:** 프런트엔드에서 백엔드 통신 오류를 표현하는 예외입니다.
> > > > > - **상속:** `RuntimeError`
> > > > > - **클래스 호출 결과:** `ApiError` 객체. 초기화 메서드 자체의 반환값과는 다릅니다.
> > > > > - **직접 정의한 메서드:** 없음
> > > > > - **생성 매개변수:** 부모 예외의 *args를 사용합니다. 이 프로젝트는 주로 오류 메시지를 전달합니다.
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/core/api_client.py:41` — `_request` / 직접 호출
> > > > > - `FastApi/frontend/core/api_client.py:45` — `_request` / 직접 호출
> > > > > - `FastApi/frontend/core/api_client.py:53` — `_request` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:33` — `_metrics_row` / 참조·타입·콜백 등
> > > > > - `FastApi/frontend/views/documents.py:103` — `render` / 참조·타입·콜백 등
> > > > > - `FastApi/frontend/views/login.py:28` — `render` / 참조·타입·콜백 등
> > > > >
> > > > > **직접 정의한 메서드:** 없음. 생성·상속 규칙은 위 설명을 참고하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] _request</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:16`
> > > > > - **역할·로직:** HTTP URL·헤더·파라미터를 구성해 요청하고, 연결·시간초과·HTTP 오류를 ApiError로 바꾸며 JSON 응답을 반환합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `method` | `str` | `필수` | `위치/키워드` | HTTP 요청 방식 |
> > > > > | `path` | `str` | `필수` | `위치/키워드` | 읽을 파일 경로 또는 HTTP 경로(함수 역할 참고) |
> > > > > | `params` | `dict \| None` | `None` | `키워드 전용` | HTTP 쿼리 파라미터 |
> > > > > | `json` | `dict \| None` | `None` | `키워드 전용` | HTTP 요청 JSON 본문 |
> > > > > | `emp_no` | `str \| None` | `None` | `키워드 전용` | 사용자 사번 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `Any`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return response.json()
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _request(
> > > > > >     method: str,  # GET,POST 전송방식 
> > > > > >     path: str,    # BASE_URL 뒤에 붙는 경로 ex. /api/v1/documents
> > > > > >     *,
> > > > > >     params: dict | None = None,  # 쿼리스트링 ?aaa=10
> > > > > >     json: dict | None = None,    # 요청 본문으로 보낼 dict 타입 데이터 
> > > > > >     emp_no: str | None = None,   # 사원번호. X-Emp-No 헤더값 
> > > > > > ) -> Any:
> > > > > >
> > > > > >     clean_params = None
> > > > > >     if params is not None: # 파라미터가 있다면 
> > > > > >         # None,빈문자열,전체라는 값이 아닌 파라미터값들만 파라미터로 취합 
> > > > > >         clean_params = {k: v for k, v in params.items() if v not in (None, "", "전체")}
> > > > > >
> > > > > >     # emp_no가 넘어오면 헤더 정보로 추가 
> > > > > >     headers = {"X-Emp-No": emp_no} if emp_no else None
> > > > > >     # 요청할 URL 완성 
> > > > > >     url = f"{BASE_URL}{path}"
> > > > > >
> > > > > >     try:
> > > > > >         # 백엔드에 요청 
> > > > > >         response = httpx2.request(
> > > > > >             method, url, params=clean_params, json=json, headers=headers, timeout=TIMEOUT
> > > > > >         )
> > > > > >     except httpx2.ConnectError as exc:
> > > > > >         raise ApiError(
> > > > > >             f"백엔드에 연결하지 못했습니다. 터미널에서 서버가 떠 있는지 확인하세요 ({BASE_URL})."
> > > > > >         ) from exc
> > > > > >     except httpx2.TimeoutException as exc:
> > > > > >         raise ApiError("응답이 너무 늦습니다. 서버가 멎었는지 확인하세요.") from exc
> > > > > >
> > > > > >     # 요청 4xx, 5xx 발생시 
> > > > > >     if response.status_code >= 400:
> > > > > >         try:
> > > > > >             message = response.json().get("message") or response.text
> > > > > >         except ValueError:
> > > > > >             message = response.text
> > > > > >         raise ApiError(message)
> > > > > >
> > > > > >     # 응답 데이터 리턴 
> > > > > >     return response.json()
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/core/api_client.py:60` — `login` / 직접 호출
> > > > > - `FastApi/frontend/core/api_client.py:64` — `me` / 직접 호출
> > > > > - `FastApi/frontend/core/api_client.py:83` — `list_documents` / 직접 호출
> > > > > - `FastApi/frontend/core/api_client.py:87` — `get_document` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] login</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:59`
> > > > > - **역할·로직:** 로그인 API에 사번과 비밀번호를 POST로 전송합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `emp_no` | `str` | `필수` | `위치/키워드` | 사용자 사번 |
> > > > > | `password` | `str` | `필수` | `위치/키워드` | 로그인 입력 비밀번호 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return _request('POST', '/api/v1/auth/login', json={'emp_no': emp_no, 'password': password})
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def login(emp_no: str, password: str) -> dict:
> > > > > >     return _request("POST", "/api/v1/auth/login", json={"emp_no": emp_no, "password": password})
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/login.py:24` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] me</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:63`
> > > > > - **역할·로직:** 사번을 헤더에 넣어 현재 사용자 조회 API를 호출합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `emp_no` | `str` | `필수` | `위치/키워드` | 사용자 사번 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return _request('GET', '/api/v1/auth/me', emp_no=emp_no)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def me(emp_no: str) -> dict:
> > > > > >     return _request("GET", "/api/v1/auth/me", emp_no=emp_no)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] list_documents</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:67`
> > > > > - **역할·로직:** HTTP API를 호출해 문서 목록을 필터 조건으로 조회합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `dept_id` | `str \| None` | `None` | `키워드 전용` | 부서 식별자 또는 필터 |
> > > > > | `security_level` | `str \| None` | `None` | `키워드 전용` | 문서 보안 등급 또는 필터 |
> > > > > | `status` | `str \| None` | `None` | `키워드 전용` | 문서 상태 필터 또는 테스트의 기대 HTTP 상태 코드 |
> > > > > | `q` | `str \| None` | `None` | `키워드 전용` | 문서 제목·ID 검색어 |
> > > > > | `limit` | `int` | `20` | `키워드 전용` | 최대 조회 건수 |
> > > > > | `emp_no` | `str \| None` | `None` | `키워드 전용` | 사용자 사번 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `list[dict]`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return _request('GET', '/api/v1/documents', params=params, emp_no=emp_no)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def list_documents(
> > > > > >     *,
> > > > > >     dept_id: str | None = None,
> > > > > >     security_level: str | None = None,
> > > > > >     status: str | None = None,
> > > > > >     q: str | None = None,
> > > > > >     limit: int = 20,
> > > > > >     emp_no: str | None = None, # 신원 함께 보내기 
> > > > > > ) -> list[dict]:
> > > > > >     params = {
> > > > > >         "dept_id": dept_id,
> > > > > >         "security_level": security_level,
> > > > > >         "status": status,
> > > > > >         "q" : q,
> > > > > >         "limit": limit
> > > > > >     }
> > > > > >     return _request("GET", "/api/v1/documents", params=params, emp_no=emp_no)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/core/api_client.py:91` — `stats` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:101` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>6. [독립 함수] get_document</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:86`
> > > > > - **역할·로직:** HTTP API를 호출해 문서 한 건을 조회합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `doc_id` | `str` | `필수` | `위치/키워드` | 문서 식별자 |
> > > > > | `emp_no` | `str \| None` | `None` | `키워드 전용` | 사용자 사번 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return _request('GET', f'/api/v1/documents/{doc_id}', emp_no=emp_no)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def get_document(doc_id: str, *, emp_no: str | None = None) -> dict:
> > > > > >     return _request("GET", f"/api/v1/documents/{doc_id}", emp_no=emp_no)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>7. [독립 함수] stats</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/api_client.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/api_client.py:90`
> > > > > - **역할·로직:** 문서 목록을 가져와 전체·현행·만료·재임베딩 개수를 집계합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `emp_no` | `str \| None` | `None` | `키워드 전용` | 사용자 사번 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return {'total': len(rows), 'current': sum((1 for row in rows if row['status'] == '현행')), 'expired': sum((1 for row in rows if row['status'] == '만료')), 'reindexing': sum((1 for row in rows if row['index_status'] == '재임베딩 '))}
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def stats(*, emp_no: str | None = None) -> dict:
> > > > > >     rows = list_documents(limit=100, emp_no=emp_no)
> > > > > >     return {
> > > > > >         "total": len(rows), 
> > > > > >         "current": sum(1 for row in rows if row["status"] == "현행"), 
> > > > > >         "expired": sum(1 for row in rows if row["status"] == "만료"),
> > > > > >         "reindexing" : sum(1 for row in rows if row["index_status"] == "재임베딩 ")
> > > > > >     }
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/documents.py:32` — `_metrics_row` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/core/router.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `current_page`, `go`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] current_page</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/router.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/router.py:7`
> > > > > - **역할·로직:** 세션에 저장된 현재 화면 이름을 읽습니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return st.session_state.get('page', 'login')
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def current_page() -> str:
> > > > > >     return st.session_state.get("page", "login")
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:79` — `main` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] go</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/router.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/router.py:11`
> > > > > - **역할·로직:** 세션의 화면 이름을 바꾸고 화면을 다시 실행하도록 요청합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `page` | `str` | `필수` | `위치/키워드` | 이동할 화면 이름 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def go(page: str) -> None:
> > > > > >     st.session_state["page"] = page
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - 범위 안에서 이름이 해석되는 직접 호출·참조를 찾지 못했습니다. 위 자동 호출 설명과 아래 후보를 함께 확인하세요.
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/core/session.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `init_state`, `current_user`, `is_authenticated`, `login`, `logout`, `emp_no`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] init_state</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:16`
> > > > > - **역할·로직:** 세션에 없는 상태 키에 초기값을 채웁니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def init_state() -> None:
> > > > > >     for key, value in DEFAULTS.items():
> > > > > >         # 화면 리런되어도 데이터 유지되는 변수들 초기화 
> > > > > >         st.session_state.setdefault(key, value)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:68` — `main` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] current_user</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:22`
> > > > > - **역할·로직:** 세션의 사용자 dict 또는 None을 가져옵니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict \| None`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return st.session_state.get('user')
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def current_user() -> dict | None:
> > > > > >     return st.session_state.get("user")
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:40` — `render_sidebar` / 직접 호출
> > > > > - `FastApi/frontend/core/session.py:27` — `is_authenticated` / 직접 호출
> > > > > - `FastApi/frontend/core/session.py:43` — `emp_no` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] is_authenticated</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:26`
> > > > > - **역할·로직:** 현재 사용자 정보가 있는지 확인합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `bool`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return current_user() is not None
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def is_authenticated() -> bool:
> > > > > >     return current_user() is not None
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:71` — `main` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] login</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:30`
> > > > > - **역할·로직:** 사용자 dict를 세션에 저장하고 문서 화면으로 전환할 상태를 지정합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `user` | `dict` | `필수` | `위치/키워드` | 사용자 dict 또는 User 객체(타입 참고) |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def login(user: dict) -> None:
> > > > > >     st.session_state["user"] = user
> > > > > >     st.session_state["page"] = "documents"
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/login.py:32` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] logout</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:35`
> > > > > - **역할·로직:** 로그인 사용자와 문서 필터를 초기화하고 로그인 화면 상태로 바꿉니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def logout() -> None:
> > > > > >     st.session_state["user"] = None
> > > > > >     st.session_state["page"] = "login"
> > > > > >     for key in ("f_dept", "f_level", "f_status", "f_q"):
> > > > > >         st.session_state[key] = DEFAULTS[key]
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:53` — `render_sidebar` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>6. [독립 함수] emp_no</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/core/session.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/core/session.py:42`
> > > > > - **역할·로직:** 현재 사용자의 사번을 반환합니다. 비로그인이면 None입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str \| None`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return user['emp_no'] if user else None
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def emp_no() -> str | None:
> > > > > >     user = current_user() 
> > > > > >     return user["emp_no"] if user else None
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/documents.py:32` — `_metrics_row` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:102` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/frontend/ui</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/__init__.py</h1></summary>
> > > >
> > > > 직접 정의한 함수·클래스: **없음**.
> > > >
> > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/badge.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `tone_for`, `badge_html`, `badge`, `badges`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] tone_for</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/badge.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/badge.py:18`
> > > > > - **역할·로직:** 상태 문구의 접두어에 맞는 배지 색상 이름을 찾습니다. 없으면 neutral입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return tone
> > > > > return 'neutral'
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def tone_for(text: str) -> str:
> > > > > >     for key, tone in _TONE_BY_TEXT.items():
> > > > > >         if text.startswith(key):
> > > > > >             return tone
> > > > > >     return "neutral"
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:9` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/badge.py:27` — `badge_html` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] badge_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/badge.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/badge.py:25`
> > > > > - **역할·로직:** 문구를 HTML 이스케이프하고 배지 HTML 문자열을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > > | `tone` | `str \| None` | `None` | `위치/키워드` | 표시 색상·상태 스타일 이름 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return f'<span class="ag-badge ag-badge--{tone}">{html.escape(str(text))}</span>'
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def badge_html(text: str, tone: str | None = None) -> str:
> > > > > >     """배지 HTML 문자열. 표 셀 안에 넣을 때 쓴다."""
> > > > > >     tone = tone or tone_for(text)
> > > > > >     if tone not in _TONES:
> > > > > >         tone = "neutral"
> > > > > >     return f'<span class="ag-badge ag-badge--{tone}">{html.escape(str(text))}</span>'
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:9` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/badge.py:34` — `badge` / 직접 호출
> > > > > - `FastApi/frontend/ui/badge.py:38` — `badges` / 직접 호출
> > > > > - `FastApi/frontend/ui/card.py:9` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/card.py:86` — `page_header` / 직접 호출
> > > > > - `FastApi/frontend/ui/source.py:8` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/source.py:26` — `source_html` / 직접 호출
> > > > > - `FastApi/frontend/ui/source.py:28` — `source_html` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:57` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:61` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:78` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:79` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:80` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:130` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:8` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/views/documents.py:78` — `_table` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:81` — `_table` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] badge</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/badge.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/badge.py:33`
> > > > > - **역할·로직:** 배지 하나를 Streamlit 화면에 출력합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > > | `tone` | `str \| None` | `None` | `위치/키워드` | 표시 색상·상태 스타일 이름 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def badge(text: str, tone: str | None = None) -> None:
> > > > > >     st.markdown(badge_html(text, tone), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:9` — `모듈 import` / import/재공개
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] badges</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/badge.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/badge.py:37`
> > > > > - **역할·로직:** 여러 배지를 HTML로 이어 붙여 화면에 출력합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[tuple[str, str \| None]]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def badges(items: list[tuple[str, str | None]]) -> None:
> > > > > >     st.markdown(" ".join(badge_html(t, tone) for t, tone in items), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:9` — `모듈 import` / import/재공개
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/card.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `inline_md`, `card_html`, `card`, `bordered`, `note`, `message_block`, `log_block`, `meta_footer`, `page_header`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] inline_md</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:12`
> > > > > - **역할·로직:** 텍스트를 이스케이프한 뒤 굵게 표시와 줄바꿈만 HTML로 변환합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return out.replace('\n\n', '<br><br>').replace('\n', '<br>')
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def inline_md(text: str) -> str:
> > > > > >     """**굵게** 와 줄바꿈만 HTML 로 바꾼다.
> > > > > >
> > > > > >     HTML 블록(.ag-note 등) 안에 넣는 문장은 Streamlit 이 마크다운을 처리해 주지 않는다.
> > > > > >     전체 마크다운 파서를 넣을 일은 아니라서 두 가지만 처리한다.
> > > > > >     """
> > > > > >     out = html.escape(text or "")
> > > > > >     while out.count("**") >= 2:
> > > > > >         out = out.replace("**", "<b>", 1).replace("**", "</b>", 1)
> > > > > >     return out.replace("\n\n", "<br><br>").replace("\n", "<br>")
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/card.py:56` — `note` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] card_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:24`
> > > > > - **역할·로직:** 라벨·제목·본문을 합쳐 카드 HTML 문자열을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `body` | `str` | `필수` | `위치/키워드` | 요청 모델 또는 카드 HTML 본문(타입 참고) |
> > > > > | `label` | `str \| None` | `None` | `키워드 전용` | 표시 라벨 |
> > > > > | `title` | `str \| None` | `None` | `키워드 전용` | 제목 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return ''.join(parts)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def card_html(body: str, *, label: str | None = None, title: str | None = None) -> str:
> > > > > >     parts = ['<div class="ag-card">']
> > > > > >     if label:
> > > > > >         parts.append(f'<div class="ag-card-label">{html.escape(label)}</div>')
> > > > > >     if title:
> > > > > >         parts.append(f'<div class="ag-card-title">{html.escape(title)}</div>')
> > > > > >     parts.append(body)
> > > > > >     parts.append("</div>")
> > > > > >     return "".join(parts)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/card.py:36` — `card` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] card</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:35`
> > > > > - **역할·로직:** 카드 HTML을 Streamlit 화면에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `body` | `str` | `필수` | `위치/키워드` | 요청 모델 또는 카드 HTML 본문(타입 참고) |
> > > > > | `label` | `str \| None` | `None` | `키워드 전용` | 표시 라벨 |
> > > > > | `title` | `str \| None` | `None` | `키워드 전용` | 제목 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def card(body: str, *, label: str | None = None, title: str | None = None) -> None:
> > > > > >     st.markdown(card_html(body, label=label, title=title), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:125` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] bordered</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:40`
> > > > > - **역할·로직:** 테두리 있는 Streamlit 컨테이너를 만들고 with 블록에 제공합니다.
> > > > > - **데코레이터:** `contextmanager`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `label` | `str \| None` | `None` | `위치/키워드` | 표시 라벨 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `타입 표기 없음`
> > > > > - 일반 return으로 결과를 주는 함수가 아니라 yield를 사용하는 함수입니다.
> > > > > - 호출하면 컨텍스트 매니저를 반환합니다. with/async with 진입 시 아래 값을 제공하고, 블록 종료 시 yield 뒤 정리 코드를 실행합니다.
> > > > > - 제공 값: `(yield box)`
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def bordered(label: str | None = None):
> > > > > >     """Streamlit 위젯(버튼 등)을 안에 넣어야 할 때 쓰는 테두리 컨테이너."""
> > > > > >     box = st.container(border=True)
> > > > > >     with box:
> > > > > >         if label:
> > > > > >             st.markdown(f'<div class="ag-card-label">{html.escape(label)}</div>',
> > > > > >                         unsafe_allow_html=True)
> > > > > >         yield box
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] note</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:50`
> > > > > - **역할·로직:** 지정한 색상과 선택적 간단한 마크다운 처리를 적용한 안내 블록을 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > > | `tone` | `str` | `''` | `위치/키워드` | 표시 색상·상태 스타일 이름 |
> > > > > | `markdown` | `bool` | `False` | `키워드 전용` | 굵게·줄바꿈 변환 적용 여부 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def note(text: str, tone: str = "", *, markdown: bool = False) -> None:
> > > > > >     """왼쪽 세로선이 있는 안내 블록. tone: '' | 'ok' | 'wait' | 'no'
> > > > > >
> > > > > >     markdown=True 면 **굵게** 와 줄바꿈을 해석한다.
> > > > > >     """
> > > > > >     cls = f"ag-note ag-note--{tone}" if tone else "ag-note"
> > > > > >     body = inline_md(text) if markdown else text
> > > > > >     st.markdown(f'<div class="{cls}">{body}</div>', unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:113` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>6. [독립 함수] message_block</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:60`
> > > > > - **역할·로직:** 문구를 이스케이프해 메시지 영역에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def message_block(text: str) -> None:
> > > > > >     """Slack 전송 문구처럼 '그대로 나갈 텍스트'를 보여주는 블록."""
> > > > > >     st.markdown(f'<div class="ag-msg">{html.escape(text)}</div>', unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:134` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>7. [독립 함수] log_block</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:65`
> > > > > - **역할·로직:** 로그 문자열들을 줄바꿈으로 합쳐 고정폭 표시 영역에 출력합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `lines` | `list[str]` | `필수` | `위치/키워드` | 표시할 로그 문자열 목록 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def log_block(lines: list[str]) -> None:
> > > > > >     """감사 로그 — 모노스페이스."""
> > > > > >     body = html.escape("\n".join(lines))
> > > > > >     st.markdown(f'<div class="ag-log">{body}</div>', unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:165` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>8. [독립 함수] meta_footer</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:71`
> > > > > - **역할·로직:** 응답 하단에 시간·토큰·비용 등의 메타정보 문자열을 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `text` | `str` | `필수` | `위치/키워드` | 검사·변환·표시할 문자열 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def meta_footer(text: str) -> None:
> > > > > >     """응답 하단 메타: 3.1s · 입력 4,120 tok · 42원 · haiku-4.5"""
> > > > > >     st.markdown(f'<div class="ag-meta">{html.escape(text)}</div>', unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:171` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>9. [독립 함수] page_header</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/card.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/card.py:76`
> > > > > - **역할·로직:** 경로 표시·제목·배지·부제목을 페이지 상단에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `title` | `str` | `필수` | `위치/키워드` | 제목 |
> > > > > | `crumb` | `str \| None` | `None` | `키워드 전용` | 페이지 상단의 경로 안내 문구 |
> > > > > | `subtitle` | `str \| None` | `None` | `키워드 전용` | 부제목 |
> > > > > | `badges` | `list[tuple[str, str \| None]] \| None` | `None` | `키워드 전용` | 문구와 색상으로 구성한 배지 목록 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def page_header(
> > > > > >     title: str,
> > > > > >     *,
> > > > > >     crumb: str | None = None,
> > > > > >     subtitle: str | None = None,
> > > > > >     badges: list[tuple[str, str | None]] | None = None,
> > > > > > ) -> None:
> > > > > >     out = []
> > > > > >     if crumb:
> > > > > >         out.append(f'<div class="ag-crumb">{html.escape(crumb)}</div>')
> > > > > >     chips = " ".join(badge_html(t, tone) for t, tone in (badges or []))
> > > > > >     out.append(
> > > > > >         f'<div class="ag-head"><h1 style="margin:0">{html.escape(title)}</h1>{chips}</div>'
> > > > > >     )
> > > > > >     if subtitle:
> > > > > >         out.append(f'<div class="ag-sub">{html.escape(subtitle)}</div>')
> > > > > >     st.markdown("".join(out), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:47` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/chart.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `bars`, `line`, `timeline`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] bars</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/chart.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/chart.py:13`
> > > > > - **역할·로직:** 값과 축의 비율에 맞춰 가로 막대그래프 HTML을 만들어 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[tuple[str, float]]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > > | `max_value` | `float` | `100` | `키워드 전용` | 그래프 축 최댓값 |
> > > > > | `unit` | `str` | `'%'` | `키워드 전용` | 수치 표시 단위 |
> > > > > | `strong_last` | `bool` | `True` | `키워드 전용` | 마지막 막대 강조 여부 |
> > > > > | `ticks` | `list[float] \| None` | `None` | `키워드 전용` | 그래프 축 눈금 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def bars(
> > > > > >     items: list[tuple[str, float]],
> > > > > >     *,
> > > > > >     max_value: float = 100,
> > > > > >     unit: str = "%",
> > > > > >     strong_last: bool = True,
> > > > > >     ticks: list[float] | None = None,
> > > > > > ) -> None:
> > > > > >     """가로 막대. 단일 색상, 마지막 막대만 진하게.
> > > > > >
> > > > > >     items      : [(라벨, 값)]
> > > > > >     max_value  : 축 최대값. 막대 폭 = 값 / max_value
> > > > > >     ticks      : 눈금 값. 기본 0 · 25 · 50 · 75 · 100 (max_value 기준 4등분)
> > > > > >     """
> > > > > >     ticks = ticks or [max_value * i / 4 for i in range(5)]
> > > > > >     out = ['<div class="ag-bars">']
> > > > > >
> > > > > >     last = len(items) - 1
> > > > > >     for i, (label, value) in enumerate(items):
> > > > > >         pct = 0 if max_value == 0 else max(0.0, min(100.0, value / max_value * 100))
> > > > > >         fill_cls = "ag-bar-fill ag-bar-fill--strong" if (strong_last and i == last) else "ag-bar-fill"
> > > > > >         weight = "600" if (strong_last and i == last) else "400"
> > > > > >         num = f"{value:g}{unit}"
> > > > > >         out.append(
> > > > > >             f'<div class="ag-bar-row">'
> > > > > >             f'<div class="ag-bar-label" style="font-weight:{weight}">{html.escape(label)}</div>'
> > > > > >             f'<div class="ag-bar-track"><div class="{fill_cls}" style="width:{pct:.4f}%"></div></div>'
> > > > > >             f'<div class="ag-bar-value" style="font-weight:{weight}">{html.escape(num)}</div>'
> > > > > >             f"</div>"
> > > > > >         )
> > > > > >
> > > > > >     # 축 — 막대와 같은 flex 레이아웃 위에 올린다
> > > > > >     tick_html = []
> > > > > >     for i, t in enumerate(ticks):
> > > > > >         pos = 0 if max_value == 0 else t / max_value * 100
> > > > > >         cls = "ag-bar-tick"
> > > > > >         if i == 0:
> > > > > >             cls += " ag-bar-tick--first"
> > > > > >         elif i == len(ticks) - 1:
> > > > > >             cls += " ag-bar-tick--last"
> > > > > >         tick_html.append(f'<div class="{cls}" style="left:{pos:.4f}%">{t:g}{unit}</div>')
> > > > > >     out.append(
> > > > > >         '<div class="ag-bar-row" style="margin-top:2px">'
> > > > > >         '<div class="ag-bar-label"></div>'
> > > > > >         f'<div class="ag-bar-axis-track">{"".join(tick_html)}</div>'
> > > > > >         '<div class="ag-bar-value"></div>'
> > > > > >         "</div>"
> > > > > >     )
> > > > > >     out.append("</div>")
> > > > > >     st.markdown("".join(out), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:21` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:150` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] line</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/chart.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/chart.py:65`
> > > > > - **역할·로직:** 값을 SVG 좌표로 바꿔 선·면·축·마지막 점을 표시합니다. 값 목록이 비어 있으면 바로 종료합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `values` | `list[float]` | `필수` | `위치/키워드` | 그래프의 숫자 목록 |
> > > > > | `labels` | `list[str]` | `필수` | `위치/키워드` | 그래프 가로축 라벨 목록 |
> > > > > | `y_ticks` | `list[float]` | `필수` | `키워드 전용` | 세로축 눈금 목록 |
> > > > > | `last_label` | `str \| None` | `None` | `키워드 전용` | 마지막 점에 붙일 라벨 |
> > > > > | `height` | `int` | `190` | `키워드 전용` | 그래프 높이 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def line(
> > > > > >     values: list[float],
> > > > > >     labels: list[str],
> > > > > >     *,
> > > > > >     y_ticks: list[float],
> > > > > >     last_label: str | None = None,
> > > > > >     height: int = 190,
> > > > > > ) -> None:
> > > > > >     """단일 계열 라인 + 옅은 면. 마지막 점에 마커와 라벨."""
> > > > > >     if not values:
> > > > > >         return
> > > > > >     W, H = 720, height
> > > > > >     pad_l, pad_r, pad_t, pad_b = 52, 60, 14, 26
> > > > > >     y_max = max(y_ticks) or 1
> > > > > >     inner_w = W - pad_l - pad_r
> > > > > >     inner_h = H - pad_t - pad_b
> > > > > >
> > > > > >     def x_at(i: int) -> float:
> > > > > >         return pad_l + (inner_w * i / max(1, len(values) - 1))
> > > > > >
> > > > > >     def y_at(v: float) -> float:
> > > > > >         return pad_t + inner_h - (inner_h * min(v, y_max) / y_max)
> > > > > >
> > > > > >     pts = [(x_at(i), y_at(v)) for i, v in enumerate(values)]
> > > > > >     poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
> > > > > >     area = f"{pad_l},{pad_t + inner_h} {poly} {pts[-1][0]:.1f},{pad_t + inner_h}"
> > > > > >
> > > > > >     grid, ylab = [], []
> > > > > >     for t in y_ticks:
> > > > > >         y = y_at(t)
> > > > > >         grid.append(
> > > > > >             f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l + inner_w}" y2="{y:.1f}" '
> > > > > >             f'stroke="#DCE4E1" stroke-width="1"/>'
> > > > > >         )
> > > > > >         ylab.append(
> > > > > >             f'<text x="{pad_l - 8}" y="{y + 4:.1f}" text-anchor="end" '
> > > > > >             f'font-size="11" fill="#66766F">{t:g}</text>'
> > > > > >         )
> > > > > >
> > > > > >     xlab = []
> > > > > >     step = max(1, len(labels) // 7)
> > > > > >     for i, lb in enumerate(labels):
> > > > > >         if i % step == 0 or i == len(labels) - 1:
> > > > > >             xlab.append(
> > > > > >                 f'<text x="{x_at(i):.1f}" y="{H - 6}" text-anchor="middle" '
> > > > > >                 f'font-size="11" fill="#66766F">{html.escape(lb)}</text>'
> > > > > >             )
> > > > > >
> > > > > >     lx, ly = pts[-1]
> > > > > >     marker = (
> > > > > >         f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4" fill="#0E6E62"/>'
> > > > > >         f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="7" fill="#0E6E62" opacity="0.18"/>'
> > > > > >     )
> > > > > >     if last_label:
> > > > > >         marker += (
> > > > > >             f'<text x="{lx + 10:.1f}" y="{ly + 4:.1f}" font-size="12" '
> > > > > >             f'font-weight="700" fill="#0A544A">{html.escape(last_label)}</text>'
> > > > > >         )
> > > > > >
> > > > > >     svg = f"""<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto" role="img">
> > > > > >   {''.join(grid)}
> > > > > >   <polygon points="{area}" fill="#0E6E62" opacity="0.10"/>
> > > > > >   <polyline points="{poly}" fill="none" stroke="#0E6E62" stroke-width="2"
> > > > > >             stroke-linejoin="round" stroke-linecap="round"/>
> > > > > >   {marker}{''.join(ylab)}{''.join(xlab)}
> > > > > > </svg>"""
> > > > > >     st.markdown(svg, unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:21` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:156` — `모듈 실행부` / 직접 호출
> > > > >
> > > > > **이 함수 안의 함수**
> > > > >
> > > > > - 2.1 `line.x_at`
> > > > > - 2.2 `line.y_at`
> > > > >
> > > > > <details>
> > > > > <summary><h2>2.1. [중첩 함수] line.x_at</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/frontend/ui/chart.py`
> > > > > >
> > > > > > **소속 함수:** `line`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/frontend/ui/chart.py:82`
> > > > > > - **역할·로직:** 선 그래프에서 데이터 인덱스를 가로 좌표로 변환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `i` | `int` | `필수` | `위치/키워드` | 데이터 인덱스 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `float`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return pad_l + inner_w * i / max(1, len(values) - 1)
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def x_at(i: int) -> float:
> > > > > > >         return pad_l + (inner_w * i / max(1, len(values) - 1))
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/frontend/ui/chart.py:88` — `line` / 직접 호출
> > > > > > - `FastApi/frontend/ui/chart.py:109` — `line` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > > <details>
> > > > > <summary><h2>2.2. [중첩 함수] line.y_at</h2></summary>
> > > > > >
> > > > > > **소속 파일:** `FastApi/frontend/ui/chart.py`
> > > > > >
> > > > > > **소속 함수:** `line`
> > > > > >
> > > > > > - **정의 파일:** `FastApi/frontend/ui/chart.py:85`
> > > > > > - **역할·로직:** 선 그래프에서 값을 세로 좌표로 변환합니다.
> > > > > >
> > > > > > **매개변수**
> > > > > >
> > > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > > | --- | --- | --- | --- | --- |
> > > > > > | `v` | `float` | `필수` | `위치/키워드` | 세로 좌표로 바꿀 값 |
> > > > > >
> > > > > > **반환값**
> > > > > >
> > > > > > - 선언: `float`
> > > > > > - 실제 return 표현식(분기별):
> > > > > >
> > > > > > ```python
> > > > > > return pad_t + inner_h - inner_h * min(v, y_max) / y_max
> > > > > > ```
> > > > > >
> > > > > > <details>
> > > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > > >
> > > > > > > ```python
> > > > > > > def y_at(v: float) -> float:
> > > > > > >         return pad_t + inner_h - (inner_h * min(v, y_max) / y_max)
> > > > > > > ```
> > > > > > >
> > > > > > </details>
> > > > > >
> > > > > > **호출·사용 위치**
> > > > > >
> > > > > > - `FastApi/frontend/ui/chart.py:88` — `line` / 직접 호출
> > > > > > - `FastApi/frontend/ui/chart.py:94` — `line` / 직접 호출
> > > > > >
> > > > > </details>
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] timeline</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/chart.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/chart.py:134`
> > > > > - **역할·로직:** HTML 항목 목록을 버전 타임라인으로 표시하며 첫 항목을 강조합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[str]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def timeline(items: list[str]) -> None:
> > > > > >     """버전 타임라인. items 는 이미 만들어진 HTML 조각. 첫 항목이 '현행'."""
> > > > > >     out = ['<div class="ag-tl">']
> > > > > >     for i, body in enumerate(items):
> > > > > >         cls = "ag-tl-item ag-tl-item--now" if i == 0 else "ag-tl-item"
> > > > > >         out.append(f'<div class="{cls}">{body}</div>')
> > > > > >     out.append("</div>")
> > > > > >     st.markdown("".join(out), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:21` — `모듈 import` / import/재공개
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/metric.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `metrics`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] metrics</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/metric.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/metric.py:9`
> > > > > - **역할·로직:** 라벨·값·변화량·색상이 담긴 dict 목록을 지표 타일로 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[dict]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def metrics(items: list[dict]) -> None:
> > > > > >     """
> > > > > >     items: [{label, value, delta?, tone?}]
> > > > > >       tone: '' | 'ok' | 'wait' | 'no'
> > > > > >     """
> > > > > >     out = ['<div class="ag-metrics">']
> > > > > >     for it in items:
> > > > > >         tone = it.get("tone") or ""
> > > > > >         cls = f"ag-metric ag-metric--{tone}" if tone else "ag-metric"
> > > > > >         delta = it.get("delta")
> > > > > >         delta_html = (
> > > > > >             f'<div class="ag-metric-delta" style="color:var(--ag-muted)">'
> > > > > >             f"{html.escape(str(delta))}</div>"
> > > > > >             if delta
> > > > > >             else ""
> > > > > >         )
> > > > > >         out.append(
> > > > > >             f'<div class="{cls}">'
> > > > > >             f'<div class="ag-metric-label">{html.escape(str(it["label"]))}</div>'
> > > > > >             f'<div class="ag-metric-value">{html.escape(str(it["value"]))}</div>'
> > > > > >             f"{delta_html}</div>"
> > > > > >         )
> > > > > >     out.append("</div>")
> > > > > >     st.markdown("".join(out), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:22` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:66` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:9` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/views/documents.py:37` — `_metrics_row` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/source.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `source_html`, `sources`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] source_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/source.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/source.py:11`
> > > > > - **역할·로직:** 문서 제목·버전·위치·유사도·인용문을 출처 표시용 HTML로 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `title` | `str` | `필수` | `키워드 전용` | 제목 |
> > > > > | `version` | `str` | `필수` | `키워드 전용` | 문서 버전 문자열 또는 ORM 객체(타입 참고) |
> > > > > | `locator` | `str` | `필수` | `키워드 전용` | 문서 안의 근거 위치 |
> > > > > | `score` | `float` | `필수` | `키워드 전용` | 표시할 근거 유사도 |
> > > > > | `quote` | `str \| None` | `None` | `키워드 전용` | 인용문 |
> > > > > | `extra_badge` | `tuple[str, str] \| None` | `None` | `키워드 전용` | 추가 배지의 문구와 색상 |
> > > > > | `weak` | `bool` | `False` | `키워드 전용` | 근거 부족 스타일 사용 여부 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return f'<div style="margin-bottom:var(--ag-s4)">{head}{body}</div>'
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def source_html(
> > > > > >     *,
> > > > > >     title: str,
> > > > > >     version: str,
> > > > > >     locator: str,
> > > > > >     score: float,
> > > > > >     quote: str | None = None,
> > > > > >     extra_badge: tuple[str, str] | None = None,
> > > > > >     weak: bool = False,
> > > > > > ) -> str:
> > > > > >     """
> > > > > >     weak=True 면 임계값 미달 — 빨간 유사도 배지 + 흐린 인용.
> > > > > >     extra_badge 예: ("시행 2025-07-01", "neutral")
> > > > > >     """
> > > > > >     score_tone = "no" if weak else "accent"
> > > > > >     chips = [badge_html(version, "accent"), badge_html(f"{score:.2f}", score_tone)]
> > > > > >     if extra_badge:
> > > > > >         chips.append(badge_html(*extra_badge))
> > > > > >     head = (
> > > > > >         f'<div class="ag-src-meta">{html.escape(locator)}</div>'
> > > > > >         f'<div style="font-weight:600;font-size:var(--ag-fs-sm)">{html.escape(title)} '
> > > > > >         + " ".join(chips)
> > > > > >         + "</div>"
> > > > > >     )
> > > > > >     cls = "ag-src ag-src--no" if weak else "ag-src"
> > > > > >     body = f'<div class="{cls}">{html.escape(quote)}</div>' if quote else ""
> > > > > >     return f'<div style="margin-bottom:var(--ag-s4)">{head}{body}</div>'
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:23` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/source.py:43` — `sources` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] sources</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/source.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/source.py:40`
> > > > > - **역할·로직:** 출처 목록을 source_html로 변환해 화면에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[dict]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > > | `weak` | `bool` | `False` | `키워드 전용` | 근거 부족 스타일 사용 여부 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def sources(items: list[dict], *, weak: bool = False) -> None:
> > > > > >     """items: [{title, version, locator, score, quote?, extra_badge?}]"""
> > > > > >     st.markdown(
> > > > > >         "".join(source_html(weak=weak, **item) for item in items),
> > > > > >         unsafe_allow_html=True,
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:23` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:100` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:116` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/status.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `steps_html`, `steps`, `progress`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] steps_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/status.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/status.py:11`
> > > > > - **역할·로직:** 처리 단계의 이름·상태·시간을 표시하는 HTML을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[dict]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return ''.join(out)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def steps_html(items: list[dict]) -> str:
> > > > > >     """items: [{name, state: 'ok'|'no'|'wait'|'todo', time?}]"""
> > > > > >     out = ['<div class="ag-steps">']
> > > > > >     for it in items:
> > > > > >         state = it.get("state", "todo")
> > > > > >         time = it.get("time") or ("—" if state in ("no", "todo") else "")
> > > > > >         out.append(
> > > > > >             f'<div class="ag-step ag-step--{state}">'
> > > > > >             f'<div class="ag-step-mark">{_MARK.get(state, "·")}</div>'
> > > > > >             f'<div class="ag-step-name">{html.escape(str(it["name"]))}</div>'
> > > > > >             f'<div class="ag-step-time">{html.escape(str(time))}</div>'
> > > > > >             f"</div>"
> > > > > >         )
> > > > > >     out.append("</div>")
> > > > > >     return "".join(out)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:24` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/status.py:29` — `steps` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] steps</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/status.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/status.py:28`
> > > > > - **역할·로직:** 단계 목록을 화면에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `items` | `list[dict]` | `필수` | `위치/키워드` | 표시할 항목 목록; 원소 구조는 타입과 함수 코드 참고 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def steps(items: list[dict]) -> None:
> > > > > >     st.markdown(steps_html(items), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:24` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:140` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] progress</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/status.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/status.py:32`
> > > > > - **역할·로직:** 진행률을 0~100으로 제한하고 진행 막대와 숫자를 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `pct` | `int` | `필수` | `위치/키워드` | 진행률 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def progress(pct: int) -> None:
> > > > > >     pct = max(0, min(100, int(pct)))
> > > > > >     st.markdown(
> > > > > >         f'<div class="ag-progress"><div class="ag-progress-fill" style="width:{pct}%"></div></div>'
> > > > > >         f'<div class="ag-src-meta" style="text-align:right">{pct}%</div>',
> > > > > >         unsafe_allow_html=True,
> > > > > >     )
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:24` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:147` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/table.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `_cell`, `table_html`, `table`, `kv_html`, `kv`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] _cell</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/table.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/table.py:12`
> > > > > - **역할·로직:** 표의 셀 값을 문자열로 바꾸며 옵션에 따라 HTML을 이스케이프합니다. None이면 빈 문자열입니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `value` | `Cell` | `필수` | `위치/키워드` | 변환할 값; call_port에서는 프롬프트 값 객체, score에서는 점수 |
> > > > > | `raw` | `bool` | `필수` | `키워드 전용` | 평문 비밀번호 또는 HTML 원문 허용 여부(타입 참고) |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return ''
> > > > > return str(value) if raw else html.escape(str(value))
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _cell(value: Cell, *, raw: bool) -> str:
> > > > > >     if value is None:
> > > > > >         return ""
> > > > > >     return str(value) if raw else html.escape(str(value))
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/table.py:47` — `table_html` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] table_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/table.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/table.py:18`
> > > > > - **역할·로직:** 헤더·행·정렬·행 스타일을 조합해 표 HTML을 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `headers` | `Sequence[str]` | `필수` | `위치/키워드` | 표의 열 제목 |
> > > > > | `rows` | `Iterable[Sequence[Cell]]` | `필수` | `위치/키워드` | 표의 행 목록 |
> > > > > | `row_classes` | `Sequence[str] \| None` | `None` | `키워드 전용` | 행별 CSS 클래스 |
> > > > > | `align` | `Sequence[str] \| None` | `None` | `키워드 전용` | 열별 정렬 스타일 |
> > > > > | `raw_html` | `bool` | `True` | `키워드 전용` | 셀 HTML을 그대로 사용할지 여부 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return ''.join(out)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def table_html(
> > > > > >     headers: Sequence[str],
> > > > > >     rows: Iterable[Sequence[Cell]],
> > > > > >     *,
> > > > > >     row_classes: Sequence[str] | None = None,
> > > > > >     align: Sequence[str] | None = None,
> > > > > >     raw_html: bool = True,
> > > > > > ) -> str:
> > > > > >     """
> > > > > >     headers    : 헤더 문자열
> > > > > >     rows       : 행. 셀 값에 badge_html() 결과를 그대로 넣을 수 있다 (raw_html=True)
> > > > > >     row_classes: 행마다 "ag-row-sel" / "ag-row-muted" / "ag-row-total" / ""
> > > > > >     align      : 열마다 "" 또는 "ag-num"(우측 정렬)
> > > > > >     """
> > > > > >     rows = list(rows)
> > > > > >     align = list(align) if align else [""] * len(headers)
> > > > > >     row_classes = list(row_classes) if row_classes else [""] * len(rows)
> > > > > >
> > > > > >     out = ['<div class="ag-tbl-wrap"><table class="ag-tbl"><thead><tr>']
> > > > > >     for i, h in enumerate(headers):
> > > > > >         cls = f' class="{align[i]}"' if i < len(align) and align[i] else ""
> > > > > >         out.append(f"<th{cls}>{html.escape(str(h))}</th>")
> > > > > >     out.append("</tr></thead><tbody>")
> > > > > >
> > > > > >     for r_i, row in enumerate(rows):
> > > > > >         rc = row_classes[r_i] if r_i < len(row_classes) else ""
> > > > > >         out.append(f'<tr class="{rc}">' if rc else "<tr>")
> > > > > >         for c_i, cell in enumerate(row):
> > > > > >             cls = f' class="{align[c_i]}"' if c_i < len(align) and align[c_i] else ""
> > > > > >             out.append(f"<td{cls}>{_cell(cell, raw=raw_html)}</td>")
> > > > > >         out.append("</tr>")
> > > > > >     out.append("</tbody></table></div>")
> > > > > >     return "".join(out)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:25` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/table.py:54` — `table` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] table</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/table.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/table.py:53`
> > > > > - **역할·로직:** 표 HTML을 화면에 출력합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `headers` | `타입 표기 없음` | `필수` | `위치/키워드` | 표의 열 제목 |
> > > > > | `rows` | `타입 표기 없음` | `필수` | `위치/키워드` | 표의 행 목록 |
> > > > > | `**kwargs` | `타입 표기 없음` | `0개 이상` | `추가 키워드 인자` | 하위 함수에 전달할 추가 키워드 옵션 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def table(headers, rows, **kwargs) -> None:
> > > > > >     st.markdown(table_html(headers, rows, **kwargs), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:25` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:75` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:86` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/views/documents.py:10` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/views/documents.py:84` — `_table` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] kv_html</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/table.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/table.py:57`
> > > > > - **역할·로직:** 키·값 쌍을 2열 표 HTML로 만듭니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `pairs` | `Iterable[tuple[str, Cell]]` | `필수` | `위치/키워드` | 키·값 쌍 목록 |
> > > > > | `raw_html` | `bool` | `True` | `키워드 전용` | 셀 HTML을 그대로 사용할지 여부 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return ''.join(out)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def kv_html(pairs: Iterable[tuple[str, Cell]], *, raw_html: bool = True) -> str:
> > > > > >     """키-값 2열 표. 문서 초안 카드·상세 패널에 쓴다."""
> > > > > >     out = ['<table class="ag-kv"><tbody>']
> > > > > >     for k, v in pairs:
> > > > > >         val = "" if v is None else (str(v) if raw_html else html.escape(str(v)))
> > > > > >         out.append(
> > > > > >             f'<tr><td class="ag-kv-k">{html.escape(str(k))}</td>'
> > > > > >             f'<td class="ag-kv-v">{val}</td></tr>'
> > > > > >         )
> > > > > >     out.append("</tbody></table>")
> > > > > >     return "".join(out)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:25` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui/table.py:71` — `kv` / 직접 호출
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:126` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>5. [독립 함수] kv</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/table.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/table.py:70`
> > > > > - **역할·로직:** 키·값 표를 화면에 출력합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `pairs` | `타입 표기 없음` | `필수` | `위치/키워드` | 키·값 쌍 목록 |
> > > > > | `**kwargs` | `타입 표기 없음` | `0개 이상` | `추가 키워드 인자` | 하위 함수에 전달할 추가 키워드 옵션 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def kv(pairs, **kwargs) -> None:
> > > > > >     st.markdown(kv_html(pairs, **kwargs), unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/__init__.py:25` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:7` — `모듈 import` / import/재공개
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/ui/theme.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `load_css`, `inject_css`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] load_css</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/theme.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/theme.py:21`
> > > > > - **역할·로직:** 세 CSS 파일을 순서대로 읽어 합칩니다. 결과를 캐시하며 없는 파일은 안내 주석으로 처리합니다.
> > > > > - **데코레이터:** `lru_cache(maxsize=1)`
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `str`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return '\n'.join(parts)
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def load_css() -> str:
> > > > > >     parts = []
> > > > > >     for name in FILES:
> > > > > >         path = ASSETS / name
> > > > > >         if path.exists():
> > > > > >             parts.append(f"/* ===== {name} ===== */\n{path.read_text(encoding='utf-8')}")
> > > > > >         else:  # 배포본에서 파일이 빠져도 앱이 죽지는 않게
> > > > > >             parts.append(f"/* !! {name} 없음 !! */")
> > > > > >     return "\n".join(parts)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/ui/theme.py:34` — `inject_css` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] inject_css</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/ui/theme.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/ui/theme.py:32`
> > > > > - **역할·로직:** CSS를 style 태그로 감싸 Streamlit에 적용합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def inject_css() -> None:
> > > > > >     """앱 전체에 디자인 시스템을 적용한다. 매 실행마다 호출되어야 한다."""
> > > > > >     st.markdown(f"<style>\n{load_css()}\n</style>", unsafe_allow_html=True)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:11` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/app.py:22` — `모듈 실행부` / 직접 호출
> > > > > - `FastApi/frontend/ui/__init__.py:26` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:25` — `모듈 import` / import/재공개
> > > > > - `FastApi/frontend/ui_kit_demo.py:28` — `모듈 실행부` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > </details>
> >
> > <details>
> > <summary><h1>[폴더] FastApi/frontend/views</h1></summary>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/views/__init__.py</h1></summary>
> > > >
> > > > 직접 정의한 함수·클래스: **없음**.
> > > >
> > > > 패키지 입구 또는 다른 모듈의 이름을 재공개하는 파일입니다.
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/views/documents.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `_metrics_row`, `_filter_row`, `_table`, `render`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] _metrics_row</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/views/documents.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/views/documents.py:30`
> > > > > - **역할·로직:** 문서 집계를 요청해 지표를 그립니다. 실패하면 안내 문구를 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _metrics_row() -> None:
> > > > > >     try:
> > > > > >         counts = api_client.stats(emp_no=session.emp_no())
> > > > > >     except api_client.ApiError as exc:
> > > > > >         st.caption(f"지표를 불러오지 못했습니다: {exc}")
> > > > > >         return
> > > > > >
> > > > > >     metrics([
> > > > > >         {"label": "전체", "value": counts["total"], "delta": "문서 버전 기준"},
> > > > > >         {"label": "현행", "value": counts["current"], "delta": "지금 유효한 판",
> > > > > >          "tone": "ok"},
> > > > > >         {"label": "만료", "value": counts["expired"], "delta": "지난 판",
> > > > > >          "tone": "no"},
> > > > > >         {"label": "재임베딩", "value": counts["reindexing"], "delta": "색인을 다시 만드는 중",
> > > > > >          "tone": "wait"},
> > > > > >     ])
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/documents.py:92` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>2. [독립 함수] _filter_row</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/views/documents.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/views/documents.py:48`
> > > > > - **역할·로직:** 부서·보안등급·상태·검색어 입력을 그리고 API 전달용 필터 dict를 반환합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `dict`
> > > > > - 실제 return 표현식(분기별):
> > > > >
> > > > > ```python
> > > > > return {'dept_id': DEPTS[dept_name], 'security_level': None if level == '전체' else level, 'status': None if status == '전체' else status, 'q': keyword or None}
> > > > > ```
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _filter_row() -> dict:
> > > > > >     left, middle, right, search = st.columns([1, 1, 1, 2])
> > > > > >
> > > > > >     with left:
> > > > > >         dept_name = st.selectbox("부서", list(DEPTS), key="f_dept")
> > > > > >     with middle:
> > > > > >         level = st.selectbox("보안등급", LEVELS, key="f_level")
> > > > > >     with right:
> > > > > >         status = st.selectbox("상태", STATUSES, key="f_status")
> > > > > >     with search:
> > > > > >         keyword = st.text_input("검색어", key="f_q", placeholder="문서명 또는 문서 ID")
> > > > > >
> > > > > >     return {
> > > > > >         "dept_id": DEPTS[dept_name],
> > > > > >         "security_level": None if level == "전체" else level,
> > > > > >         "status": None if status == "전체" else status,
> > > > > >         "q": keyword or None,
> > > > > >     }
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/documents.py:94` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>3. [독립 함수] _table</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/views/documents.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/views/documents.py:68`
> > > > > - **역할·로직:** 문서 dict 목록을 표 행과 배지로 변환해 화면에 표시합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > | 이름 | 타입 | 기본값/필수 | 전달 방식 | 의미 |
> > > > > | --- | --- | --- | --- | --- |
> > > > > | `documents` | `list[dict]` | `필수` | `위치/키워드` | 화면에 표시할 문서 dict 목록 |
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def _table(documents: list[dict]) -> None:
> > > > > >     rows = []
> > > > > >     for document in documents:
> > > > > >         period = f"{document['effective_from']} ~ {document['expires_at'] or '현행'}"
> > > > > >         index_label = f"{document['index_status']} {document['index_progress']}%"
> > > > > >         rows.append([
> > > > > >             escape(document["doc_id"]),
> > > > > >             escape(document["title"]),
> > > > > >             escape(document["version"]),
> > > > > >             escape(period),
> > > > > >             badge_html(document["status"]),
> > > > > >             escape(document["dept"]),
> > > > > >             escape(document["security_level"]),
> > > > > >             badge_html(index_label),
> > > > > >         ])
> > > > > >
> > > > > >     table(HEADERS, rows, align=ALIGNS)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/views/documents.py:112` — `render` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > > <details>
> > > > <summary><h2>4. [독립 함수] render</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/views/documents.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/views/documents.py:87`
> > > > > - **역할·로직:** 문서 지표·필터·목록을 표시하고 API 오류와 빈 목록을 안내합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def render() -> None:
> > > > > >     st.title("문서 관리")
> > > > > >     st.caption("상태 필터가 「전체」라 지난 판까지 함께 보입니다. "
> > > > > >                "「현행」으로 좁히면 현재 유효한 최신본만 남습니다.")
> > > > > >
> > > > > >     _metrics_row()
> > > > > >
> > > > > >     filters = _filter_row()
> > > > > >
> > > > > >     if st.button("새 문서 업로드"):
> > > > > >         st.info("업로드 화면은 W4 에 만듭니다.")
> > > > > >
> > > > > >     with st.spinner("문서를 불러오는 중입니다..."):
> > > > > >         try:
> > > > > >             documents = api_client.list_documents(**filters, limit=100,
> > > > > >                                                   emp_no=session.emp_no())
> > > > > >         except api_client.ApiError as exc:
> > > > > >             st.error(str(exc))
> > > > > >             return
> > > > > >
> > > > > >     if not documents:
> > > > > >         st.info("조건에 맞는 문서가 없습니다. 필터를 바꿔 보세요.")
> > > > > >         return
> > > > > >
> > > > > >     st.caption(f"{len(documents)}건")
> > > > > >     _table(documents)
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:82` — `main` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > > <details>
> > > <summary><h1>[파일] FastApi/frontend/views/login.py</h1></summary>
> > > >
> > > > **파일 구성**
> > > >
> > > > - 클래스: 없음
> > > > - 파일 수준 함수: `render`
> > > > - 클래스 메서드는 해당 클래스 토글 안에, 중첩 함수는 바깥 함수 토글 안에 있습니다.
> > > >
> > > >
> > > > <details>
> > > > <summary><h2>1. [독립 함수] render</h2></summary>
> > > > >
> > > > > **소속 파일:** `FastApi/frontend/views/login.py`
> > > > >
> > > > > - **정의 파일:** `FastApi/frontend/views/login.py:7`
> > > > > - **역할·로직:** 로그인 입력 폼을 그리고 API 인증 성공 시 세션에 사용자를 저장하고 화면을 다시 실행합니다.
> > > > >
> > > > > **매개변수**
> > > > >
> > > > > 없음.
> > > > >
> > > > > **반환값**
> > > > >
> > > > > - 선언: `None`
> > > > > - **반환값 없음(None)**. 화면 표시·저장·검사 등의 동작만 수행합니다. 예외가 발생하면 정상 반환하지 않습니다.
> > > > >
> > > > > <details>
> > > > > <summary>해당 함수의 실제 로직 코드 보기</summary>
> > > > > >
> > > > > > ```python
> > > > > > def render() -> None:
> > > > > >     st.title("사내 업무 에이전트")
> > > > > >     st.write("사번과 비밀번호로 로그인하세요. 계정은 강사가 나눠 준 목록에 있습니다.")
> > > > > >
> > > > > >     st.text_input("사번", key="login_emp_no", placeholder="예) 2016-0231")
> > > > > >     st.text_input("비밀번호", type="password", key="login_pw")
> > > > > >
> > > > > >     if not st.button("로그인"):
> > > > > >         return
> > > > > >
> > > > > >     try:
> > > > > >         from core import api_client
> > > > > >     except ImportError:
> > > > > >         st.info("백엔드 호출 통로(core/api_client.py)는 02번에서 붙입니다.")
> > > > > >         return
> > > > > >
> > > > > >     try:
> > > > > >         user = api_client.login(
> > > > > >             st.session_state["login_emp_no"],
> > > > > >             st.session_state["login_pw"],
> > > > > >         )
> > > > > >     except api_client.ApiError as exc:
> > > > > >         st.error(str(exc))
> > > > > >         return
> > > > > >
> > > > > >     session.login(user)
> > > > > >
> > > > > >     st.rerun()
> > > > > > ```
> > > > > >
> > > > > </details>
> > > > >
> > > > > **호출·사용 위치**
> > > > >
> > > > > - `FastApi/frontend/app.py:72` — `main` / 직접 호출
> > > > >
> > > > </details>
> > > >
> > > </details>
> > >
> > </details>
> >
> </details>
>
</details>

<details>
<summary><h1>구현상 주의점</h1></summary>
>
> - FastApi/backend/app/core/config.py는 max_tokens를 정의하지만 FastApi/backend/app/integrations/llm_claude.py의 _call은 max_token을 읽습니다. 현재 이름이 달라 호출 준비 중 속성 오류가 날 수 있습니다. 수정하지 않았습니다.
> - FastApi/backend/app/core/exceptions.py의 AuthFailed.__int__는 __init__이 아닙니다. FastApi/backend/app/services/auth_service.py의 AuthFailed()는 필수 message를 받는 부모 생성자를 사용하게 됩니다. 문서는 현재 코드를 그대로 설명했으며 이름을 수정하지 않았습니다.
> - FastApi/backend/app/services/chat_service.py의 ask는 LangChain 체인 대신 llm.answer를 직접 호출합니다. FastApi/backend/app/agent/chain.py에 함수가 존재해도 서비스에서 실행되는 것은 아닙니다.
> - FastApi/backend/app/services/chat_service.py의 스키마 검증은 답변 내용의 사실 여부까지 보장하지 않습니다. 모델 호출 예외는 스키마 재시도와 별도 경로입니다.
> - FastApi/backend/app/models/run.py의 RunStep은 정의와 메타데이터 등록이 있지만 채팅 서비스의 단계별 저장은 연결되어 있지 않습니다.
> - FastApi/backend/tests/test_layers.py는 최상단 import만 검사하므로 함수 내부 import는 검사하지 않습니다.
> - 이름이 같은 메서드 후보는 사용 사실을 확정한 목록이 아닙니다. 예를 들어 LLMPort.answer, ClaudeLLM.answer, StubLLM.answer는 같은 호출 형태를 공유하지만 실제 객체에 따라 구현이 선택됩니다.
>
</details>
