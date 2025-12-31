from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.business.services import MovieService
from app.api.schemas import (
    MovieCreate,
    MovieUpdate,
    MovieResponse,
    ActorResponse,
    RatingResponse,
)
from app.api.decorators import handle_not_found

router = APIRouter(prefix="/movies", tags=["movies"])


def convert_movie_to_response(movie, service: MovieService) -> MovieResponse:
    actors_response = [
        ActorResponse(
            id=actor.id,
            first_name=actor.first_name,
            last_name=actor.last_name,
            full_name=f"{actor.first_name} {actor.last_name}",
            birth_date=actor.birth_date,
            nationality=actor.nationality,
        )
        for actor in movie.actors
    ]

    ratings_response = [
        RatingResponse(
            id=rating.id,
            score=rating.score,
            review_text=rating.review_text,
            reviewer_email=rating.reviewer_email,
        )
        for rating in movie.ratings
    ]

    return MovieResponse(
        id=movie.id,
        title=movie.title,
        release_date=movie.release_date,
        runtime=movie.runtime,
        synopsis=movie.synopsis,
        poster_url=movie.poster_url,
        language=movie.language,
        genres=movie.genres.split(",") if movie.genres else [],
        budget=movie.budget,
        revenue=movie.revenue,
        actors=actors_response,
        ratings=ratings_response,
        average_rating=service.calculate_average_rating(movie),
    )


@router.get("", response_model=List[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    service = MovieService(db)
    movies = service.get_all_movies()
    return [convert_movie_to_response(movie, service) for movie in movies]


@router.get("/{movie_id}", response_model=MovieResponse)
@handle_not_found("Movie")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    service = MovieService(db)
    movie = service.get_movie_by_id(movie_id)
    return movie


@router.post("", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie_data: MovieCreate, db: Session = Depends(get_db)):
    service = MovieService(db)

    movie = service.create_movie(
        title=movie_data.title,
        release_date=movie_data.release_date,
        runtime=movie_data.runtime,
        synopsis=movie_data.synopsis,
        poster_url=movie_data.poster_url,
        language=movie_data.language,
        genres=movie_data.genres,
        budget=movie_data.budget,
        revenue=movie_data.revenue,
        actor_ids=movie_data.actor_ids,
    )

    return convert_movie_to_response(movie, service)


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, movie_data: MovieUpdate, db: Session = Depends(get_db)):
    service = MovieService(db)

    movie = service.update_movie(
        movie_id=movie_id,
        title=movie_data.title,
        release_date=movie_data.release_date,
        runtime=movie_data.runtime,
        synopsis=movie_data.synopsis,
        poster_url=movie_data.poster_url,
        language=movie_data.language,
        genres=movie_data.genres,
        budget=movie_data.budget,
        revenue=movie_data.revenue,
        actor_ids=movie_data.actor_ids,
    )

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with id {movie_id} not found",
        )

    return convert_movie_to_response(movie, service)


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    service = MovieService(db)
    success = service.delete_movie(movie_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with id {movie_id} not found",
        )
