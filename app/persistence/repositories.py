from typing import List, Optional
from sqlalchemy.orm import Session
from app.database.models import Movie, Actor, Rating


class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Movie]:
        return self.db.query(Movie).all()

    def get_by_id(self, movie_id: int) -> Optional[Movie]:
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def create(self, movie: Movie) -> Movie:
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def update(self, movie: Movie) -> Movie:
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def delete(self, movie: Movie) -> None:
        self.db.delete(movie)
        self.db.commit()


class ActorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Actor]:
        return self.db.query(Actor).all()

    def get_by_id(self, actor_id: int) -> Optional[Actor]:
        return self.db.query(Actor).filter(Actor.id == actor_id).first()

    def create(self, actor: Actor) -> Actor:
        self.db.add(actor)
        self.db.commit()
        self.db.refresh(actor)
        return actor

    def update(self, actor: Actor) -> Actor:
        self.db.commit()
        self.db.refresh(actor)
        return actor

    def delete(self, actor: Actor) -> None:
        self.db.delete(actor)
        self.db.commit()


class RatingRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Rating]:
        return self.db.query(Rating).all()

    def get_by_id(self, rating_id: int) -> Optional[Rating]:
        return self.db.query(Rating).filter(Rating.id == rating_id).first()

    def get_by_movie_id(self, movie_id: int) -> List[Rating]:
        return self.db.query(Rating).filter(Rating.movie_id == movie_id).all()

    def create(self, rating: Rating) -> Rating:
        self.db.add(rating)
        self.db.commit()
        self.db.refresh(rating)
        return rating

    def update(self, rating: Rating) -> Rating:
        self.db.commit()
        self.db.refresh(rating)
        return rating

    def delete(self, rating: Rating) -> None:
        self.db.delete(rating)
        self.db.commit()
