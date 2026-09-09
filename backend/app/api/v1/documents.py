from fastapi import APIRouter, Query
from typing import Annotated

# 문서 API를 모아두는 라우터
router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

# DB사용 전, 임시 데이터 추가(나중에 없앨거)
documents = [
    {
        "doc_id": "DOC-HR-014",
        "title": "2026년 휴가 운영 규정",
        "dept": "인사",
        "security_level": "일반",
        "file_format": "docx",
        "status": "active",
    },
    {
        "doc_id": "DOC-HR-021",
        "title": "복리후생 운영 지침",
        "dept": "인사",
        "security_level": "일반",
        "file_format": "pdf",
        "status": "active",
    },
    {
        "doc_id": "DOC-SE-011",
        "title": "정보보안 관리 규정",
        "dept": "보안",
        "security_level": "3급",
        "file_format": "pdf",
        "status": "active",
    },
    {
        "doc_id": "DOC-PU-007",
        "title": "구매 계약 업무 지침",
        "dept": "구매",
        "security_level": "대외비",
        "file_format": "docx",
        "status": "active",
    },
]


# 문서 목록 요청 -> prfix다음 아무것도 안할때
@router.get("")  # ...8000/documents
def list_documents(
    dept: str | None = None,
    security_level: str | None = None,
    file_format: str | None = None,
    limit: Annotated[int, Query(ge=1, le=20)] = 20,
) -> list[dict]:
    # 원본 복사
    result = documents.copy()

    # 부서 조건
    if dept is not None:
        result = [doc for doc in result if doc["dept"] == dept]

    # 보안 등급 조건
    if security_level is not None:
        result = [doc for doc in result if doc["security_level"] == security_level]

    # 파일 형식 조건
    if file_format is not None:
        result = [doc for doc in result if doc["file_format"] == file_format]

    return result[:limit]


# 문서 1개 조회 : ...8000/documents/doc_id값
@router.get("/{doc_id}")
def get_document(doc_id: str) -> dict:
    for doc in documents:
        if doc["doc_id"] == doc_id:
            return doc
    return {
        "doc_id": doc_id,
        "message": "문서를 찾지 못했습니다.",
    }
