from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(70))
    release_year: Mapped[int] = mapped_column()
    genre: Mapped[str] = mapped_column(String(100))
    producer: Mapped[str] = mapped_column(String(50))
    duration: Mapped[int] = mapped_column()
    actors: Mapped[str] = mapped_column(String(200))