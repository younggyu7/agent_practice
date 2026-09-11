from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

CLEARANCE: dict[str, int] = {"일반": 1, "3급": 2, "대외비": 3}


class Department(Base, TimestampMixin):
    __tablename__ = "departments"

    id: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    users: Mapped[list["User"]] = relationship(back_populates="dept")
    documents: Mapped[list["Document"]] = relationship(back_populates="dept")


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    emp_no: Mapped[str] = mapped_column(String(16), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    dept_id: Mapped[str] = mapped_column(ForeignKey("departments.id"))
    role: Mapped[str] = mapped_column(String(10))
    clearance: Mapped[str] = mapped_column(String(10))

    dept: Mapped["Department"] = relationship(back_populates="users")
    documents: Mapped[list["Document"]] = relationship(back_populates="owner")

    @property
    def clearance_level(self) -> int:
        return CLEARANCE.get(self.clearance, 1)

    @property
    def can_approve(self) -> bool:

        return self.role in {"팀장", "관리자"}
