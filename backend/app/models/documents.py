from __future__ import annotations

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin


class Department(Base, TimestampMixin):
    __tablename__ = "departments"
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    documents: Mapped[list["Document"]] = relationship(back_populates="department")


class Document(Base, TimestampMixin):
    __tablename__ = "documents"
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    depth_id: Mapped[str] = mapped_column(ForeignKey("departments.id"), index=True)
    security_leve: Mapped[str] = mapped_column(String(20), default="일반", index=True)
    # 연관된 ORM 객체를 양방향으로 탐색할 관계 만듬 -> 상호 연결시 해당 클래스에도 기입
    department: Mapped[Department] = relationship(back_populates="documents")
    version: Mapped[list["DocumentVersion"]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )
