from typing import List, Optional
from datetime import date
from sqlalchemy.orm import Session
from app.database.models import Movie, Actor, Rating
from app.persistence.repositories import MovieRepository, ActorRepository, RatingRepository


class MovieService:
    def __init__(self, db: Session):
        self.repository = MovieRepository(db)
        self.actor_repository = ActorRepository(db)
        self.db = db

    def get_all_movies(self) -> List[Movie]:
        return self.repository.get_all()

    def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        return self.repository.get_by_id(movie_id)

    def create_movie(
        self,
        title: str,
        release_date: date,
        runtime: int,
        language: str,
        synopsis: Optional[str] = None,
        poster_url: Optional[str] = None,
        genres: Optional[List[str]] = None,
        budget: Optional[float] = None,
        revenue: Optional[float] = None,
        actor_ids: Optional[List[int]] = None,
    ) -> Movie:
        movie = Movie(
            title=title,
            release_date=release_date,
            runtime=runtime,
            synopsis=synopsis,
            poster_url=poster_url,
            language=language,
            genres=','.join(genres) if genres else None,
            budget=budget,
            revenue=revenue,
        )

        if actor_ids:
            actors = [self.actor_repository.get_by_id(actor_id) for actor_id in actor_ids]
            actors = [actor for actor in actors if actor is not None]
            movie.actors = actors

        return self.repository.create(movie)

    def update_movie(
        self,
        movie_id: int,
        title: Optional[str] = None,
        release_date: Optional[date] = None,
        runtime: Optional[int] = None,
        synopsis: Optional[str] = None,
        poster_url: Optional[str] = None,
        language: Optional[str] = None,
        genres: Optional[List[str]] = None,
        budget: Optional[float] = None,
        revenue: Optional[float] = None,
        actor_ids: Optional[List[int]] = None,
    ) -> Optional[Movie]:
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            return None

        if title is not None:
            movie.title = title
        if release_date is not None:
            movie.release_date = release_date
        if runtime is not None:
            movie.runtime = runtime
        if synopsis is not None:
            movie.synopsis = synopsis
        if poster_url is not None:
            movie.poster_url = poster_url
        if language is not None:
            movie.language = language
        if genres is not None:
            movie.genres = ','.join(genres)
        if budget is not None:
            movie.budget = budget
        if revenue is not None:
            movie.revenue = revenue

        if actor_ids is not None:
            actors = [self.actor_repository.get_by_id(actor_id) for actor_id in actor_ids]
            actors = [actor for actor in actors if actor is not None]
            movie.actors = actors

        return self.repository.update(movie)

    def delete_movie(self, movie_id: int) -> bool:
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            return False
        self.repository.delete(movie)
        return True

    def calculate_average_rating(self, movie: Movie) -> Optional[float]:
        if not movie.ratings:
            return None
        total = sum(rating.score for rating in movie.ratings)
        return round(total / len(movie.ratings), 1)


class ActorService:
    def __init__(self, db: Session):
        self.repository = ActorRepository(db)

    def get_all_actors(self) -> List[Actor]:
        return self.repository.get_all()

    def get_actor_by_id(self, actor_id: int) -> Optional[Actor]:
        return self.repository.get_by_id(actor_id)

    def create_actor(
        self,
        first_name: str,
        last_name: str,
        birth_date: Optional[date] = None,
        nationality: Optional[str] = None,
    ) -> Actor:
        actor = Actor(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            nationality=nationality,
        )
        return self.repository.create(actor)

    def update_actor(
        self,
        actor_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        birth_date: Optional[date] = None,
        nationality: Optional[str] = None,
    ) -> Optional[Actor]:
        actor = self.repository.get_by_id(actor_id)
        if not actor:
            return None

        if first_name is not None:
            actor.first_name = first_name
        if last_name is not None:
            actor.last_name = last_name
        if birth_date is not None:
            actor.birth_date = birth_date
        if nationality is not None:
            actor.nationality = nationality

        return self.repository.update(actor)

    def delete_actor(self, actor_id: int) -> bool:
        actor = self.repository.get_by_id(actor_id)
        if not actor:
            return False
        self.repository.delete(actor)
        return True


class RatingService:
    def __init__(self, db: Session):
        self.repository = RatingRepository(db)
        self.movie_repository = MovieRepository(db)

    def get_all_ratings(self) -> List[Rating]:
        return self.repository.get_all()

    def get_rating_by_id(self, rating_id: int) -> Optional[Rating]:
        return self.repository.get_by_id(rating_id)

    def get_ratings_by_movie(self, movie_id: int) -> List[Rating]:
        return self.repository.get_by_movie_id(movie_id)

    def create_rating(
        self,
        score: float,
        movie_id: int,
        review_text: Optional[str] = None,
        reviewer_email: Optional[str] = None,
    ) -> Optional[Rating]:
        movie = self.movie_repository.get_by_id(movie_id)
        if not movie:
            return None

        rating = Rating(
            score=score,
            review_text=review_text,
            reviewer_email=reviewer_email,
            movie_id=movie_id,
        )
        return self.repository.create(rating)

    def update_rating(
        self,
        rating_id: int,
        score: Optional[float] = None,
        review_text: Optional[str] = None,
        reviewer_email: Optional[str] = None,
    ) -> Optional[Rating]:
        rating = self.repository.get_by_id(rating_id)
        if not rating:
            return None

        if score is not None:
            rating.score = score
        if review_text is not None:
            rating.review_text = review_text
        if reviewer_email is not None:
            rating.reviewer_email = reviewer_email

        return self.repository.update(rating)

    def delete_rating(self, rating_id: int) -> bool:
        rating = self.repository.get_by_id(rating_id)
        if not rating:
            return False
        self.repository.delete(rating)
        return True
