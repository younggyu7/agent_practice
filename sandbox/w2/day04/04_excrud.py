from sqlalchemy import and_, desc, func, or_, select

from demo_models import Document, Department, SessionLocal, reset_db, seed


def main() -> None:
    reset_db()
    seed()  # 샘플 데이터

    with SessionLocal() as session:
        stmt = select(Document).join(Document.department)
        print(
            "문서의 id와 부서명",
            [(d.id, d.department) for d in session.scalars(stmt)],
        )
        stmt = (
            select(Document)
            .join(Document.department)
            .where(Department.name == "보안팀")
        )
        print(
            "보안팀의 문서의 id와 부서명",
            [(d.id, d.department) for d in session.scalars(stmt)],
        )


if __name__ == "__main__":
    main()
