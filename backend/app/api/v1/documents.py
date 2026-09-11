from fastapi import APIRouter, Query, File, Form, UploadFile
from typing import Annotated

import shutil
from datetime import date
from pathlib import Path

from app.schemas.document import DocumentOut, DocumentCreateOut
from app.api.v1.deps import SettingsDep, LoggerDep
from app.core.exceptions import NotFound, ValidationFailed
from app.services import document_service

# 문서 API를 모아두는 라우터
router = APIRouter(prefix="/documents", tags=["documents"])

# 파일 업로드될 경로 지정
UPLOAD_DIR = Path("uploads")

ALLOWED_EXTS = {".docx",".pdf"}


# DB사용 전, 임시 데이터 추가 (나중에 없앨거)
_DOCS: list[dict] = [
    {
        "doc_id": "DOC-HR-014",
        "title": "2026년 휴가 운영 규정",
        "dept": "인사",
        "version": "v2.0",
        "security_level": "일반",
        "file_format": "docx",
        "status": "active",
        "secret_note": "담당자 메모 - 개정 예고",
    },
    {
        "doc_id": "DOC-HR-021",
        "title": "복리후생 운영 지침",
        "dept": "인사",
        "version": "v2.1",
        "security_level": "일반",
        "file_format": "pdf",
        "status": "active",
        "secret_note": "담당자 메모 - 인사팀 검토중",
    },
    {
        "doc_id": "DOC-SE-011",
        "title": "정보보안 관리 규정",
        "dept": "보안",
        "version": "v1.5",
        "security_level": "3급",
        "file_format": "pdf",
        "status": "active",
        "secret_note": "담당자 메모 - 열람 이력 점검 필요",
    },
    {
        "doc_id": "DOC-PU-007",
        "title": "구매 계약 업무 지침",
        "dept": "구매",
        "version": "v3.0",
        "security_level": "대외비",
        "file_format": "docx",
        "status": "active",
        "secret_note": "담당자 메모 - v4.0 준비중",
    },
]


# 문서 목록 요청
@router.get("", response_model=list[DocumentOut])  # ...8000/api/v1/documents
def list_documents(
    # settings: SettingsDep,  # 의존성 주입: 별칭으로 처리
    # dept: str | None = None,
    # security_level: str | None = None,
    # file_format: str | None = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> list[dict]:
    # result = _DOCS.copy()

    # if dept is not None:
    #     result = [doc for doc in result if doc["dept"] == dept]

    # if security_level is not None:
    #     result = [doc for doc in result if doc["security_level"] == security_level]

    # if file_format is not None:
    #     result = [doc for doc in result if doc["file_format"] == file_format]

    # return result[:limit]

    # database와 연결 (service-> repository- > DB 데이터 조회)
    return document_service.list_documents(limit=limit)

# 문서 등록
@router.post("", response_model=DocumentCreateOut, status_code=201)
async def upload_document(
    doc_id: Annotated[str, Form()],
    title: Annotated[str, Form()],
    dept_id: Annotated[str, Form()],
    security_level: Annotated[str, Form()],
    version: Annotated[str, Form()],
    effective_from: Annotated[date, Form()],
    file: Annotated[UploadFile, File()],
    logger: LoggerDep,
)->dict:
    safe_name = Path(file.filename or "").name
    ext = Path(safe_name).suffix.lower() # 확장자명을 가져온다

    # 우리가 지정한 docx/pdf 아니면 파일 업로드 처리 X
    if ext not in ALLOWED_EXTS:    
        raise ValidationFailed(
            f"{ext or '확장자 없는'} 파일은 등록할 수 없습니다. "
            "DOCX 또는 PDF 로 변환해 다시 올려 주세요."
        )
    
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    # 경로/파일명.확장자 : 저장할 파일명은 우리가 짓는다.
    dest = UPLOAD_DIR / f"{doc_id}_{version}{ext}"

    # 파일을 조금씩 나눠서 업로드한다.
    with dest.open("wb") as out:
        shutil.copyfileobj(file.file, out) # 실제 파일을 dest (저장위치 + 파일명) 으로 복사하는 코드

    logger.info("문서 파일 저장: %s (%s)", dest, security_level)

    # DB에 파일정보 저장하고, 돌려받은 정보(응답데이터) 화면에 돌려주기
    return document_service.create_document(
        doc_id=doc_id,
        title=title,
        dept_id=dept_id,
        security_level=security_level,
        version=version,
        effective_from=effective_from,
        file_path=dest.as_posix(),
        file_format=ext.lstrip("."),
    )




# # 예외 테스트
# @router.get("/find")
# def find_doc():
#     raise NotFound("문서 못 찾음")


# 문서 1개 조회  : ...8000/api/v1/documents/문서id값
@router.get("/{doc_id}", response_model=DocumentOut)
def get_document(doc_id: str) -> dict:
    for doc in _DOCS:
        if doc["doc_id"] == doc_id:
            return doc

    raise NotFound(f"문서를 찾지 못했습니다.: {doc_id}")


# 잘못된 예시
/
"""
@router.get("/List")
def get_list(
    dept_id=None,
    security_level=None,
    status=None,
    q=None,
):
    sql = "SELECT * FROM documents WHERE 1=1"
    if dept_id:
        sql += f" AND dept_id = '{dept_id}'"
    if security_level:
        sql += f" AND secuirty_level = '{secuirty_level}'"
    # ...
    session.excute(sql)
    # 로직처리
    # DB접속해서 쿼리문 실행
    # 돌려받은 데이터를 활용해서 다른 로직
    # 데이터 리턴
"""