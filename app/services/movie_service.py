from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import Movie
from ..schemas import MovieCreate, MovieUpdate

def create_movie(session: Session, payload: MovieCreate) -> Movie:
    movie = Movie(**payload.model_dump())
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

def get_movie(session: Session, movie_id: int) -> Movie | None:
    return session.get(Movie, movie_id)

def get_movies(
    session: Session,
    title: str | None = None,
    limit: int = 10,
    offset: int = 0,
) -> list[Movie]:
    stmt = select(Movie)
    if title is not None:
        stmt = stmt.where(Movie.title == title)
    stmt = stmt.limit(limit).offset(offset)
    return list(session.scalars(stmt).all())

def update_movie(session: Session, movie: Movie, payload: MovieUpdate) -> Movie:
    changes = payload.model_dump(exclude_unset=True)
    for field, value in changes.items():
        setattr(movie, field, value)
    session.commit()
    session.refresh(movie)
    return movie

def delete_movie(session: Session, movie: Movie) -> None:
    session.delete(movie)
    session.commit()