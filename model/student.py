from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Student(Base):
    __tablename__ = "students"
    id : Mapped[int] = mapped_column(primary_key = True)
    name : Mapped[str] = mapped_column(String(100))
    rank : Mapped[int]
    age : Mapped[int]
    email : Mapped[str] = mapped_column(String(100), unique = True)