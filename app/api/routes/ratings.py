from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.business.services import RatingService
from app.api.schemas import RatingCreate, RatingUpdate, RatingResponse

router = APIRouter(prefix="/ratings", tags=["ratings"])


def convert_rating_to_response(rating) -> RatingResponse:
    return RatingResponse(
        id=rating.id,
        score=rating.score,
        review_text=rating.review_text,
        reviewer_email=rating.reviewer_email
    )


@router.get("", response_model=List[RatingResponse])
def get_ratings(db: Session = Depends(get_db)):
    service = RatingService(db)
    ratings = service.get_all_ratings()
    return [convert_rating_to_response(rating) for rating in ratings]


@router.get("/{rating_id}", response_model=RatingResponse)
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    service = RatingService(db)
    rating = service.get_rating_by_id(rating_id)
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with id {rating_id} not found"
        )
    return convert_rating_to_response(rating)


@router.post("", response_model=RatingResponse, status_code=status.HTTP_201_CREATED)
def create_rating(rating_data: RatingCreate, db: Session = Depends(get_db)):
    service = RatingService(db)
    rating = service.create_rating(
        score=rating_data.score,
        movie_id=rating_data.movie_id,
        review_text=rating_data.review_text,
        reviewer_email=rating_data.reviewer_email
    )
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with id {rating_data.movie_id} not found"
        )
    return convert_rating_to_response(rating)


@router.put("/{rating_id}", response_model=RatingResponse)
def update_rating(rating_id: int, rating_data: RatingUpdate, db: Session = Depends(get_db)):
    service = RatingService(db)
    rating = service.update_rating(
        rating_id=rating_id,
        score=rating_data.score,
        review_text=rating_data.review_text,
        reviewer_email=rating_data.reviewer_email
    )
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with id {rating_id} not found"
        )
    return convert_rating_to_response(rating)


@router.delete("/{rating_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    service = RatingService(db)
    success = service.delete_rating(rating_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with id {rating_id} not found"
        )
