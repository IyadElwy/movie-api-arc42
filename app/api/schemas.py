from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ActorReference(BaseModel):
    actor_id: int = Field(alias="actorId")
    href: str

    class Config:
        populate_by_name = True


class RatingReference(BaseModel):
    rating_id: int = Field(alias="ratingId")
    href: str

    class Config:
        populate_by_name = True


class ActorBase(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    birth_date: Optional[date] = Field(None, alias="birthDate")
    nationality: Optional[str] = None

    class Config:
        populate_by_name = True


class ActorCreate(ActorBase):
    pass


class ActorUpdate(BaseModel):
    first_name: Optional[str] = Field(None, alias="firstName")
    last_name: Optional[str] = Field(None, alias="lastName")
    birth_date: Optional[date] = Field(None, alias="birthDate")
    nationality: Optional[str] = None

    class Config:
        populate_by_name = True


class ActorResponse(ActorBase):
    id: int
    full_name: str = Field(alias="fullName")

    class Config:
        populate_by_name = True
        from_attributes = True


class RatingBase(BaseModel):
    score: float = Field(ge=0, le=10)
    review_text: Optional[str] = Field(None, alias="reviewText")
    reviewer_email: Optional[EmailStr] = Field(None, alias="reviewerEmail")

    class Config:
        populate_by_name = True


class RatingCreate(RatingBase):
    movie_id: int = Field(alias="movieId")

    class Config:
        populate_by_name = True


class RatingUpdate(BaseModel):
    score: Optional[float] = Field(None, ge=0, le=10)
    review_text: Optional[str] = Field(None, alias="reviewText")
    reviewer_email: Optional[EmailStr] = Field(None, alias="reviewerEmail")

    class Config:
        populate_by_name = True


class RatingResponse(RatingBase):
    id: int

    class Config:
        populate_by_name = True
        from_attributes = True


class MovieBase(BaseModel):
    title: str
    release_date: date = Field(alias="releaseDate")
    runtime: int
    synopsis: Optional[str] = None
    poster_url: Optional[str] = Field(None, alias="posterUrl")
    language: str
    genres: Optional[List[str]] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None

    class Config:
        populate_by_name = True


class MovieCreate(MovieBase):
    actor_ids: Optional[List[int]] = Field(None, alias="actorIds")

    class Config:
        populate_by_name = True


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    release_date: Optional[date] = Field(None, alias="releaseDate")
    runtime: Optional[int] = None
    synopsis: Optional[str] = None
    poster_url: Optional[str] = Field(None, alias="posterUrl")
    language: Optional[str] = None
    genres: Optional[List[str]] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None
    actor_ids: Optional[List[int]] = Field(None, alias="actorIds")

    class Config:
        populate_by_name = True


class MovieResponse(MovieBase):
    id: int
    actors: List[ActorResponse]
    ratings: List[RatingResponse]
    average_rating: Optional[float] = Field(None, alias="averageRating")

    class Config:
        populate_by_name = True
        from_attributes = True
