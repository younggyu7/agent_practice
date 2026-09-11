# 문서 관련 쿼리문을 모아 둔곳. (DB요청)
from __future__ import annotations

from sqlalchemy import Row, desc, or_, select
from sqlalchemy.orm import Session, joinedload

from app.models.document import Document, DocumentVersion


# 문서 목록 조회
def list_documents(
    session: Session,  # DB 세션 : 서비스에서 전달해줄거임
    *,
    dept_id: str | None = None,
    security_level: str | None = None,
    status: str | None = None,
    q: (
        str | None
    ) = None,  # 문서명, 문서번호에 이 글자가 들어간 것만 조회(검색 기능 때 사용)
    limit: int = 50,
) -> list[Row]:

    # 쿼리문
    stmt = select(DocumentVersion, Document).join(
        Document, DocumentVersion.doc_id == Document.id
    )

    if dept_id:
        stmt = stmt.where(Document.dept_id == dept_id)
    if security_level:
        stmt = stmt.where(Document.security_level == security_level)
    if status:
        stmt = stmt.where(DocumentVersion.status == status)
    if q:
        stmt = stmt.where(
            or_(Document.title.ilike(f"%{q}%"), Document.id.ilike(f"%{q}%"))
        )

    # 로딩 전력 : 즉시 로딩 : 부서 테이블도 조인해서 함께 가져오기
    stmt = stmt.options(joinedload(Document.dept))
    # 정렬, 개수 제한
    stmt = stmt.order_by(Document.id, desc(DocumentVersion.version)).limit(limit)
    # 최종 결과 리스트로 만드렁 리턴
    return list(session.execute(stmt).all())


# 문서 id로 문서 한개 조회
def get_document(session: Session, doc_id: str) -> Document | None:
    return session.get(Document, doc_id)


# 특정 문서에 문서에 버전 한개 추가
def add_version(session: Session, doc: Document, **fields) -> DocumentVersion:
    version = DocumentVersion(doc_id=doc.id, **fields)
    session.add(version)
    session.flush()
    return version
