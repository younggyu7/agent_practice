from __future__ import annotations

import os
from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine, event, text
from sqlalchemy.orm import Session, sessionmaker

# DB 경로 : 환경변수 참고, 없으면 app.db사용
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")


# 엔진 생성
def build_engine() -> Engine:

    options: dict = {"pool_pre_ping": True}

    if DATABASE_URL.startswith("sqlite"):  # sqlite라면
        options["connect_args"] = {"check_same_thread": False}  # 스레드 체크 옵션 추가

    db_engine = create_engine(DATABASE_URL, **options)  # 엔진 생성 : 옵션 풀어서 주기

    if DATABASE_URL.startswith("sqlite"):
        # sqlite 라면 외래키 검사 설정 추가
        @event.listens_for(db_engine, "connect")
        def enable_foreign_keys(dbapi_connection, _connection_record) -> None:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

    return db_engine


# 세션 공장 생성 : 어플리케이션 전체에서 하나만 만듬
engine = build_engine()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


# 편의 함수
@contextmanager
def session_scope() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def main() -> None:
    print("DB URL: ", engine.url)
    print("DB 종류: ", engine.dialect.name)

    with session_scope() as session:
        print("select 결과:", session.execute(text("SELECT 1")).scalar_one())


if __name__ == "__main__":
    main()
