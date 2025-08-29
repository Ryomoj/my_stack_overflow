from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class AnswersOrm(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"))
    user_id: Mapped[str]  # UUID
    text: Mapped[str] = mapped_column(String(3000))
    created_at: Mapped[datetime]
