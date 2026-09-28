# FastApi 프로젝트 구조와 기능 정리

확인일: 2026-09-29

현재 파일과 코드 연결을 기준으로 정리한 문서입니다. 파일이 있다는 사실과 실제 요청 처리에 연결되어 있다는 사실을 구분합니다. 프로그램 실행이나 DB 상태 검증을 수행한 결과는 아닙니다.

## 1. 전체 폴더·파일 구조

요청에 따라 `venv`와 앞서 제외한 `sandbox`는 생략했습니다. 자동 생성되는 `__pycache__`와 `.pytest_cache`의 내부 파일도 생략했습니다. `.pytest_cache`는 접근이 제한되어 내부를 확인하지 못했습니다. 아래 트리의 경로는 프로젝트 루트 기준이며, `PROJECT_STRUCTURE.md`는 이 문서입니다.

```text
FastApi/
├── PROJECT_STRUCTURE.md
├── .env
├── docker-compose.yml
├── pyproject.toml
├── app.db
├── netstat
├── backend/
│   ├── alembic.ini
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── auth.py
│   │   │       ├── chat.py
│   │   │       ├── documents.py
│   │   │       └── deps.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── exceptions.py
│   │   │   ├── guards.py
│   │   │   ├── logging.py
│   │   │   └── security.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── chat.py
│   │   │   ├── common.py
│   │   │   └── document.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── chat_service.py
│   │   │   ├── document_service.py
│   │   │   └── ids.py
│   │   ├── repositories/
│   │   │   ├── document_repo.py
│   │   │   └── user_repo.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── document.py
│   │   │   ├── org.py
│   │   │   ├── run.py
│   │   │   └── usage.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── session.py
│   │   │   ├── init_db.py
│   │   │   ├── seed.py
│   │   │   ├── seed_data.py
│   │   │   └── migrations/
│   │   │       ├── README
│   │   │       ├── env.py
│   │   │       ├── script.py.mako
│   │   │       └── versions/
│   │   │           ├── df6947bee893_initial_schema.py
│   │   │           ├── 5b1740bb3da0_add_runs_and_run_steps.py
│   │   │           └── 0f82d3f2c172_add_usage_logs.py
│   │   ├── integrations/
│   │   │   ├── __init__.py
│   │   │   ├── ports.py
│   │   │   ├── factory.py
│   │   │   ├── llm_claude.py
│   │   │   └── langfuse_client.py
│   │   └── agent/
│   │       ├── chain.py
│   │       └── prompts/
│   │           └── answer_system.md
│   └── tests/
│       ├── conftest.py
│       ├── test_core_config.py
│       ├── test_exceptions.py
│       ├── test_guards.py
│       ├── test_health.py
│       ├── test_layers.py
│       ├── test_chat_golden.py
│       └── golden/
│           └── chat_golden.json
└── frontend/
    ├── app.py
    ├── ui_kit_demo.py
    ├── .streamlit/
    │   └── config.toml
    ├── core/
    │   ├── __init__.py
    │   ├── api_client.py
    │   ├── router.py
    │   └── session.py
    ├── views/
    │   ├── __init__.py
    │   ├── login.py
    │   └── documents.py
    ├── ui/
    │   ├── __init__.py
    │   ├── theme.py
    │   ├── badge.py
    │   ├── card.py
    │   ├── chart.py
    │   ├── metric.py
    │   ├── source.py
    │   ├── status.py
    │   └── table.py
    └── assets/
        ├── tokens.css
        ├── base.css
        └── components.css
```

## 2. 기능별 폴더·파일 설명

### 2-1. 루트: 프로젝트 설정과 실행 환경

| 파일 | 역할 |
| --- | --- |
| `.env` | DB 접속 주소, 실행 모드, 외부 서비스 키 등 환경별 설정을 보관합니다. 실제 비밀값은 이 문서에 싣지 않습니다. |
| `docker-compose.yml` | PostgreSQL과 Langfuse 컨테이너의 실행 설정입니다. PostgreSQL은 5432, Langfuse는 3000 포트를 사용하도록 구성되어 있습니다. |
| `pyproject.toml` | pytest가 `backend`를 파이썬 모듈 검색 경로로, `backend/tests`를 테스트 위치로 사용하도록 설정합니다. |
| `app.db` | 로컬 SQLite DB 파일입니다. 파일이 존재한다고 현재 프로그램이 SQLite를 사용한다는 뜻은 아닙니다. 실제 연결은 설정값으로 결정됩니다. |
| `netstat` | 이전에 저장된 네트워크 상태 출력 파일입니다. 애플리케이션 실행 모듈은 아닙니다. |
| `PROJECT_STRUCTURE.md` | 전체 구조, 각 파일의 역할, 실행 흐름을 정리한 현재 문서입니다. |

현재 설정의 `env_file=".env"`는 실행 위치의 영향을 받습니다. 루트에서 실행한다면 루트의 `.env`를 읽는 구성이 됩니다.

### 2-2. `backend/app/main.py`: FastAPI 시작점

FastAPI 애플리케이션을 만들고 필요한 기능들을 등록하는 입구입니다.

- 서버 시작 시 로깅을 설정합니다.
- `/health` 상태 확인 API를 제공합니다.
- 인증, 문서, 채팅 라우터를 `/api/v1` 아래에 연결합니다.
- 프로젝트 예외와 요청 검증 오류를 HTTP 응답으로 변환하는 전역 핸들러를 등록합니다.

`main.py`가 직접 모델을 호출하는 구조는 아닙니다. 요청을 받을 라우터와 공통 처리 기능을 연결합니다.

### 2-3. `api`: HTTP 요청을 받는 라우터

| 파일 | 역할 |
| --- | --- |
| `api/v1/auth.py` | 로그인 요청과 현재 사용자 조회 요청을 받아 인증 서비스에 전달합니다. |
| `api/v1/chat.py` | 질문을 받아 `chat_service.ask()`를 호출하고, 실행 번호로 기록을 조회합니다. |
| `api/v1/documents.py` | 문서 목록, 상세 조회, 파일 업로드 요청을 처리합니다. |
| `api/v1/deps.py` | 설정, 요청 ID, 로거, DB 세션 등 라우터에서 사용할 공통 의존성을 제공합니다. |

주요 API:

| 경로 | 기능 |
| --- | --- |
| `POST /api/v1/auth/login` | 로그인 |
| `GET /api/v1/auth/me` | 사용자 정보 조회 |
| `GET /api/v1/documents` | 문서 목록 조회 |
| `POST /api/v1/documents` | 문서 업로드 |
| `GET /api/v1/documents/{doc_id}` | 문서 한 건 조회 |
| `POST /api/v1/chat/messages` | 질문 처리 |
| `GET /api/v1/chat/runs/{run_id}` | 질문 실행 기록 조회 |

라우터는 요청을 받아 서비스에 넘기는 역할입니다. 모델 재시도나 최종 답변 저장은 서비스가 담당합니다.

### 2-4. `core`: 공통 설정·예외·입력 검사

| 파일 | 역할 |
| --- | --- |
| `config.py` | `Settings`로 환경변수와 `.env`를 읽습니다. `get_settings()`가 설정 객체를 캐시합니다. |
| `exceptions.py` | `GuardTripped`, `RateLimited`, `NotFound`, `ExternalServiceError` 등 프로젝트 예외를 정의합니다. |
| `guards.py` | 질문 길이, 허용 모델, 일일 호출 한도를 검사하는 함수를 제공합니다. |
| `logging.py` | 로그 출력 형식을 설정하고 모듈별 로거를 제공합니다. |
| `security.py` | 비밀번호 해시 생성과 검증을 담당합니다. |

현재 채팅 흐름에는 `check_question()`이 연결되어 있습니다. `check_model()`과 `check_daily_limit()`은 정의되어 있지만 현재 `ask()`에서 호출하지 않습니다.

### 2-5. `schemas`: 요청·응답 데이터의 규격

Pydantic 모델로 입력과 출력에 필요한 필드 및 타입을 정의합니다.

| 파일 | 역할 |
| --- | --- |
| `auth.py` | 로그인 입력 `LoginIn`과 사용자 출력 `UserOut`을 정의합니다. |
| `chat.py` | 질문 `ChatRequest`, 출처 `AnswerSource`, 모델 답변 `AnswerOut`, 최종 응답 `AskOut`을 정의합니다. |
| `common.py` | 상태 확인과 오류 응답의 공통 규격을 정의합니다. |
| `document.py` | 문서 조회와 생성 결과의 응답 규격을 정의합니다. |

채팅 규격의 관계:

```text
ChatRequest                 사용자 → 서버
  question

AnswerSource                출처 한 건
  doc_id / title / version / locator

AnswerOut                   모델 답변을 검증할 규격
  answer / sources / enough_evidence

AskOut(AnswerOut)            서버 → 사용자 최종 응답
  위 필드 + run_id / attempts / fallback_used
```

스키마 검증은 필드와 타입, 등록된 문서 ID 등의 규칙을 확인합니다. 답변 내용이 실제 문서와 일치하는지까지 자동으로 증명하지는 않습니다.

### 2-6. `services`: 업무 처리와 전체 실행 순서

| 파일 | 역할 |
| --- | --- |
| `auth_service.py` | 사용자 조회와 비밀번호 확인을 거쳐 로그인 결과를 만듭니다. |
| `document_service.py` | 문서 목록·상세 조회, 문서 생성 및 버전 추가 등의 업무 처리를 담당합니다. |
| `chat_service.py` | 질문 검사, 어댑터 호출, 검증, 재시도, 폴백, 실행 기록 및 사용량 저장을 연결합니다. |
| `ids.py` | 기존 실행 번호를 조회해 다음 `RUN-숫자` 값을 만듭니다. |

`chat_service.py`의 주요 함수:

| 함수 | 역할 |
| --- | --- |
| `_hint_from()` | Pydantic 오류 목록을 다음 시도에서 모델에게 전달할 문장으로 바꿉니다. |
| `_fallback()` | 근거 부족 안내를 담은 최종 `AskOut`을 만듭니다. |
| `_record_usage()` | 어댑터가 반환한 토큰 사용량과 추정 비용을 저장합니다. 저장 실패는 로그를 남기고 넘어갑니다. |
| `ask()` | 질문 한 건의 처리 순서를 관리합니다. 현재 하네스의 핵심 흐름입니다. |
| `get_run()` | 실행 번호에 해당하는 DB 기록을 찾아 반환합니다. 없으면 `NotFound`를 발생시킵니다. |

현재 `next_run_id()`는 기존 번호의 최댓값에 1을 더합니다. 여러 요청이 동시에 실행될 때 같은 번호가 만들어질 가능성은 별도로 해결해야 합니다.

### 2-7. `repositories`와 `models`: DB 조회와 테이블 정의

#### `repositories`: DB에서 어떻게 조회·저장할지

| 파일 | 역할 |
| --- | --- |
| `user_repo.py` | 사번으로 사용자 레코드를 조회합니다. |
| `document_repo.py` | 문서 목록 필터링, 문서 한 건 조회, 버전 추가 등 DB 작업을 수행합니다. |

#### `models`: DB에 어떤 형태로 저장할지

| 파일 | 주요 모델과 역할 |
| --- | --- |
| `base.py` | SQLAlchemy 모델의 공통 부모 `Base`와 생성·수정 시각용 `TimestampMixin`입니다. |
| `org.py` | `Department`, `User`와 보안 등급 관련 정보를 정의합니다. |
| `document.py` | 문서 자체인 `Document`와 개별 버전인 `DocumentVersion`을 정의합니다. |
| `run.py` | 질문 한 건의 실행 기록 `Run`과 단계 한 건의 기록 `RunStep`을 정의합니다. |
| `usage.py` | 모델 호출 사용량과 추정 비용을 저장하는 `UsageLog`를 정의합니다. |
| `__init__.py` | 모델들을 한곳에서 가져올 수 있도록 공개합니다. 모델 등록에도 관련됩니다. |

실행 기록의 관계:

```text
Run 한 건: 질문 하나의 전체 실행
├── RunStep 한 건: 실행 안의 단계 하나
├── RunStep 한 건: 다음 단계 하나
├── UsageLog 한 건: 모델 호출 한 번의 사용량
└── UsageLog 한 건: 재시도 호출 한 번의 사용량
```

이는 테이블의 연결 관계입니다. 현재 채팅 서비스는 `Run`과 `UsageLog`를 저장하지만 `RunStep`을 추가하는 코드는 아직 연결되어 있지 않습니다.

### 2-8. `db`: 연결·초기 데이터·스키마 변경

| 파일 | 역할 |
| --- | --- |
| `session.py` | DB 엔진과 세션을 만들고 재사용합니다. `session_scope()`는 정상 종료 시 커밋, 오류 시 롤백하고 세션을 닫습니다. |
| `init_db.py` | SQLAlchemy 모델을 기준으로 없는 테이블을 생성합니다. |
| `seed_data.py` | 초기 부서·사용자·문서 등에 사용할 샘플 데이터를 보관합니다. |
| `seed.py` | 초기 데이터를 DB에 넣는 작업을 담당합니다. |
| `migrations/env.py` | Alembic에 DB 접속 정보와 모델 메타데이터를 연결합니다. |
| `migrations/script.py.mako` | 새 마이그레이션 파일을 생성할 때 사용하는 템플릿입니다. |
| `migrations/README` | 마이그레이션 디렉터리의 안내 파일입니다. |
| `backend/alembic.ini` | Alembic 실행 설정과 마이그레이션 위치를 지정합니다. |

마이그레이션 이력:

| 파일 | 변경 내용 |
| --- | --- |
| `df6947bee893_initial_schema.py` | 초기 테이블 구성 |
| `5b1740bb3da0_add_runs_and_run_steps.py` | `runs`, `run_steps` 추가 |
| `0f82d3f2c172_add_usage_logs.py` | `usage_logs` 추가 |

`init_db.py`의 테이블 생성과 Alembic의 버전 관리는 별개입니다. 테이블이 존재해도 Alembic 적용 버전이 자동으로 기록되는 것은 아닙니다. 위 파일 목록만으로 현재 DB에 어디까지 적용됐는지는 판단할 수 없습니다.

### 2-9. `integrations`: 외부 서비스 연결

| 파일 | 역할 |
| --- | --- |
| `ports.py` | `LLMPort`로 어댑터의 호출 규약을, `LLMResult`로 공통 반환 형태를 정의합니다. |
| `factory.py` | 설정에 따라 사용할 어댑터를 제공합니다. 현재 live에서는 캐시된 `ClaudeLLM`을 반환하고 mock에서는 예외를 발생시킵니다. |
| `llm_claude.py` | Claude SDK 호출, 프롬프트 구성, 응답 텍스트·토큰 추출, 시간·비용 계산, `LLMResult` 변환을 담당합니다. JSON 추출 함수도 여기에 있습니다. |
| `langfuse_client.py` | Langfuse 클라이언트 생성, trace 생성과 score 기록을 감쌉니다. 관측 연결 실패는 로그를 남기고 요청 처리를 계속하도록 구성되어 있습니다. |

포트와 어댑터의 연결:

```text
factory.get_llm()
    ↓ ClaudeLLM 객체 반환
서비스가 llm.answer(question=..., contexts=..., user=...) 호출
    ↓ 실제 객체의 메서드 실행
ClaudeLLM이 Claude API 호출
    ↓ 응답을 공통 형태로 변환
LLMResult(text, model, 토큰, 비용, 시간)
    ↓
서비스가 결과 검증 및 저장
```

`LLMPort`는 호출을 대신 실행하는 객체가 아니라 규약입니다. `LLMResult`는 공통 결과 상자이고, `AnswerOut`은 그 안의 답변 텍스트를 JSON으로 해석한 후 검사할 규격입니다.

Langfuse의 `trace()`는 `yield`에서 서비스의 `with` 블록에 제어를 넘깁니다. 현재 코드에서는 상세 단계나 개별 모델 호출을 자동으로 모두 기록하는 기능까지 연결된 것은 아닙니다.

### 2-10. `agent`: LangChain 체인과 프롬프트

| 파일 | 역할 |
| --- | --- |
| `chain.py` | `LLMPort`를 LangChain Runnable로 감싸 프롬프트·호출·파서를 연결하는 함수를 제공합니다. |
| `prompts/answer_system.md` | 답변 방식, 근거 사용, JSON 출력 규칙 등 모델에게 전달할 시스템 지침입니다. |

`chain.py`의 함수:

| 함수 | 만드는 것 또는 반환값 |
| --- | --- |
| `load_prompt()` | 프롬프트 파일을 읽은 문자열 |
| `build_prompt()` | 시스템 메시지와 질문 칸을 가진 `ChatPromptTemplate` |
| `build_result_chain()` | 프롬프트 → 어댑터 호출 → `LLMResult`를 반환하는 체인 |
| `build_answer_chain()` | 위 결과에서 `text`를 추출하는 체인 |
| `build_parsed_chain()` | 답변 문자열을 지정한 Pydantic 모델로 파싱하는 체인 |

현재 `chat_service.ask()`는 `llm.answer()`를 직접 호출합니다. 따라서 이 체인 파일은 준비되어 있지만 실제 채팅 서비스 흐름에는 아직 연결되지 않았습니다. LangGraph 그래프도 현재 파일 목록에는 없습니다.

### 2-11. `backend/tests`: 테스트와 골든셋

| 파일 | 역할 |
| --- | --- |
| `conftest.py` | 테스트에서 공통으로 사용할 fixture와 준비 작업을 정의합니다. |
| `test_core_config.py` | 설정 관련 동작을 확인합니다. |
| `test_exceptions.py` | 프로젝트 예외 관련 동작을 확인합니다. |
| `test_guards.py` | 질문 공백 제거, 길이 제한, 허용 모델, 호출 한도 검사를 확인합니다. |
| `test_health.py` | 상태 확인 API를 테스트합니다. |
| `test_layers.py` | 계층 간 import 규칙을 검사합니다. 검사 코드가 탐지하는 범위 안에서 확인됩니다. |
| `test_chat_golden.py` | 골든셋 사례를 읽어 가짜 어댑터로 서비스의 검증·재시도·폴백 동작을 확인합니다. |
| `golden/chat_golden.json` | 질문, 미리 정한 모델 응답, 기대 조건으로 구성된 11개 사례입니다. |

골든셋 테스트의 실행:

```text
사례 하나 읽기
    ↓
StubLLM에 미리 정한 응답 목록 넣기
    ↓
factory.get_llm()이 StubLLM을 반환하도록 임시 교체
    ↓
실제 chat_service.ask() 실행
    ↓
출처·포함 문구·시도 횟수·폴백 여부 등을 기대 조건과 비교
```

가드 예외 사례는 별도 분기로 처리합니다. 이 테스트는 실제 Claude의 답변 품질보다 서비스가 주어진 응답을 어떻게 처리하는지 확인하는 데 초점이 있습니다. LLM을 가짜로 교체해도 현재 서비스의 DB 저장까지 자동으로 가짜가 되지는 않습니다.

### 2-12. `frontend`: Streamlit 시작점과 화면

| 파일 | 역할 |
| --- | --- |
| `app.py` | 화면 설정, CSS 적용, 로그인 상태 확인, 사이드바, 현재 화면 선택을 담당합니다. |
| `ui_kit_demo.py` | 공통 UI 부품의 모양과 사용 예시를 확인하는 데모입니다. |
| `.streamlit/config.toml` | Streamlit 설정을 보관합니다. |
| `views/login.py` | 사번·비밀번호 입력과 로그인 처리를 담당하는 화면입니다. |
| `views/documents.py` | 문서 통계, 필터, 목록을 보여주는 문서 관리 화면입니다. |

현재 연결된 화면은 로그인과 문서 관리입니다. AI 업무 도우미, 승인함, 운영 대시보드는 메뉴만 준비되어 있고 연결할 화면이 지정되지 않았습니다. 채팅 화면인 `assistant.py`는 현재 없습니다.

### 2-13. `frontend/core`: API 통신·화면 이동·사용자 상태

| 파일 | 역할 |
| --- | --- |
| `api_client.py` | HTTP 요청과 오류 처리를 공통화하고 로그인, 사용자 조회, 문서 목록·상세·집계 함수를 제공합니다. |
| `router.py` | 현재 페이지를 읽고 이동할 페이지를 지정합니다. |
| `session.py` | Streamlit 세션에 사용자, 로그인 여부, 현재 화면 등의 상태를 보관합니다. |

여기서 `session.py`는 화면의 사용자 상태입니다. 백엔드 `db/session.py`의 DB 세션과는 역할이 다릅니다.

현재 `api_client.py`에는 채팅 API 호출 함수가 없습니다. 문서 통계 함수는 문서 목록을 가져와 프런트엔드에서 집계합니다.

### 2-14. `frontend/ui`: 재사용할 화면 부품

| 파일 | 역할 |
| --- | --- |
| `theme.py` | CSS 파일을 읽어 화면에 적용합니다. |
| `badge.py` | 상태나 분류를 짧게 표시하는 배지입니다. |
| `card.py` | 카드, 안내문, 메시지, 로그 영역, 페이지 제목 등의 표시를 담당합니다. |
| `chart.py` | 막대·선 그래프와 타임라인을 표시합니다. |
| `metric.py` | 주요 수치를 묶어서 보여줍니다. |
| `source.py` | 답변의 근거 문서와 출처를 표시하는 부품입니다. |
| `status.py` | 단계별 상태와 진행률을 표시합니다. |
| `table.py` | 표와 키·값 목록을 표시합니다. |
| `__init__.py` | 공통 UI 함수를 한곳에서 가져올 수 있도록 공개합니다. |

예를 들어 출처 표시 부품이 존재해도 채팅 화면이 연결되었다는 뜻은 아닙니다. 화면을 만들 때 가져다 쓸 수 있는 준비된 부품입니다.

### 2-15. `frontend/assets`: 화면 스타일

| 파일 | 역할 |
| --- | --- |
| `tokens.css` | 색상, 간격 등 공통 디자인 값을 정의합니다. |
| `base.css` | 화면의 기본 스타일을 정의합니다. |
| `components.css` | 카드, 배지, 표 등 부품별 스타일을 정의합니다. |

### 2-16. 각 폴더의 `__init__.py`: 패키지 입구

파이썬 패키지를 구성하거나 외부에 공개할 이름을 모으는 파일입니다. 모든 `__init__.py`가 업무 로직을 담는 것은 아닙니다. 특히 `models/__init__.py`와 `frontend/ui/__init__.py`는 여러 클래스·함수를 모아서 가져오게 하는 역할이 있습니다.

## 3. 현재 요청의 실제 실행 흐름

### 3-1. 로그인·문서 조회

```text
브라우저
    ↓
Streamlit app.py
    ↓
views/login.py 또는 views/documents.py
    ↓
frontend/core/api_client.py
    ↓ HTTP 요청
FastAPI main.py → api/v1의 라우터
    ↓
auth_service 또는 document_service
    ↓
user_repo 또는 document_repo
    ↓
SQLAlchemy 모델·DB 세션 → DB
    ↓
조회 결과 → 서비스 → 라우터 → 프런트엔드 화면
```

### 3-2. 채팅 API

```text
POST /api/v1/chat/messages
    ↓
ChatRequest 요청 검증
    ↓
api/v1/chat.py → chat_service.ask()
    ↓
check_question(): 공백 정리·질문 길이 검사
    ↓
factory.get_llm(): 어댑터 준비
    ↓
run_id 생성 → Run을 '진행중'으로 저장
    ↓
Langfuse trace 시작 시도
    ↓
최대 3회 반복
    ├── 질문과 재시도 힌트 구성
    ├── ClaudeLLM.answer() → Claude 호출 → LLMResult
    ├── UsageLog 저장 시도
    ├── JSON 추출 → AnswerOut 검증
    ├── 실패: 오류 힌트를 만들어 다음 시도
    └── 성공: AskOut 생성 후 반복 종료
    ↓
3회 모두 검증 실패했다면 폴백 AskOut 생성
    ↓
Run에 최종 답변·출처·시간·'완료' 저장
    ↓
AskOut 반환
```

이 흐름은 채팅 API 기준입니다. 현재 프런트엔드에는 이 API를 호출하는 채팅 화면이 없습니다. 모델 호출 자체의 예외는 위 스키마 재시도 처리에 포함되지 않습니다.

## 4. 하네스 관점에서 현재 어디까지 만들어졌나

하네스는 모델 주변에서 호출·검증·반복·종료·기록을 관리하는 코드입니다. 현재는 `chat_service.py`가 중심이고 가드, 어댑터, 스키마, DB 및 관측 모듈이 이를 지원합니다.

| 기능 | 담당 위치 | 현재 연결 상태 |
| --- | --- | --- |
| 질문 검사 | `core/guards.py` | 서비스에서 사용 |
| 어댑터 선택 | `integrations/factory.py` | 서비스에서 사용 |
| 모델 호출 | `integrations/llm_claude.py` | 서비스에서 직접 호출 |
| JSON 추출·형식 검증 | `_extract_json()`와 `AnswerOut` | 서비스에서 사용 |
| 검증 실패 재시도 | `chat_service.ask()` | 최대 3회 호출 |
| 정상 종료·폴백 종료 | `chat_service.ask()` | 성공 시 종료, 검증 실패 소진 시 폴백 |
| 실행 기록 | `Run` | 시작과 최종 결과 저장 |
| 사용량 기록 | `UsageLog` | 모델 응답을 받은 후 저장 시도 |
| 관측 | `langfuse_client.py` | 기본 trace와 폴백 시 점수 기록 |
| 실행 단계 기록 | `RunStep` | 모델 정의만 존재, 채팅 저장 미연결 |
| 허용 모델·일일 한도 검사 | `core/guards.py` | 함수는 존재, 채팅 호출 미연결 |
| LangChain 체인 | `agent/chain.py` | 함수는 존재, 채팅 호출 미연결 |
| 문서 검색·RAG | 문서 관련 코드 및 향후 검색 흐름 | 현재 채팅은 `contexts=[]` 전달 |
| 도구 선택·실행 및 반복 | 향후 Agent 흐름 | 현재 채팅에 미구현 |
| LangGraph 상태 흐름 | 향후 그래프 | 현재 미구현 |

현재는 **모델 호출 → 형식 검증 → 재시도 → 폴백 → 결과 저장**을 관리하는 흐름이 연결된 상태입니다. 도구를 선택하고 실행 결과를 보며 반복하는 Agent 흐름까지 완성된 상태는 아닙니다.

## 5. 현재 구조를 읽을 때 기억할 점

1. **스키마 통과와 사실 검증은 다릅니다.** 출처 필드가 있어도 실제 조항이 답변을 뒷받침하는지는 별도 확인이 필요합니다.
2. **문서 관리와 RAG 검색은 다릅니다.** 문서 테이블과 목록 화면은 있지만 채팅에 검색 결과를 넣는 흐름은 아직 없습니다.
3. **실행 기록과 상세 단계 기록은 다릅니다.** `Run` 저장은 연결되어 있지만 `RunStep` 저장은 아직 없습니다.
4. **모델 호출 오류의 상태 처리가 남아 있습니다.** 호출 중 예외가 나면 현재 코드는 `Run`을 실패 상태로 바꾸지 않아 '진행중'으로 남을 수 있습니다.
5. **현재 사용자 정보는 임시값입니다.** 채팅 서비스의 기본 `user_id=1`과 모델에 전달하는 `DEFAULT_USER`를 실제 로그인 사용자와 연결하는 작업이 남아 있습니다.
6. **관측 코드를 감쌌다고 모든 단계가 기록되지는 않습니다.** 현재 trace 생성 외에 개별 호출과 검증 단계의 상세 기록은 추가 연결이 필요합니다.

이 문서 작성에서는 기존 코드를 수정하지 않았으며, 테스트 실행·서버 실행·DB 변경은 수행하지 않았습니다.
