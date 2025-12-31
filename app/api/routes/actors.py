from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.business.services import ActorService
from app.api.schemas import ActorCreate, ActorUpdate, ActorResponse

router = APIRouter(prefix="/actors", tags=["actors"])


def convert_actor_to_response(actor) -> ActorResponse:
    return ActorResponse(
        id=actor.id,
        first_name=actor.first_name,
        last_name=actor.last_name,
        full_name=f"{actor.first_name} {actor.last_name}",
        birth_date=actor.birth_date,
        nationality=actor.nationality
    )


@router.get("", response_model=List[ActorResponse])
def get_actors(db: Session = Depends(get_db)):
    service = ActorService(db)
    actors = service.get_all_actors()
    return [convert_actor_to_response(actor) for actor in actors]


@router.get("/{actor_id}", response_model=ActorResponse)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    service = ActorService(db)
    actor = service.get_actor_by_id(actor_id)
    if not actor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Actor with id {actor_id} not found"
        )
    return convert_actor_to_response(actor)


@router.post("", response_model=ActorResponse, status_code=status.HTTP_201_CREATED)
def create_actor(actor_data: ActorCreate, db: Session = Depends(get_db)):
    service = ActorService(db)
    actor = service.create_actor(
        first_name=actor_data.first_name,
        last_name=actor_data.last_name,
        birth_date=actor_data.birth_date,
        nationality=actor_data.nationality
    )
    return convert_actor_to_response(actor)


@router.put("/{actor_id}", response_model=ActorResponse)
def update_actor(actor_id: int, actor_data: ActorUpdate, db: Session = Depends(get_db)):
    service = ActorService(db)
    actor = service.update_actor(
        actor_id=actor_id,
        first_name=actor_data.first_name,
        last_name=actor_data.last_name,
        birth_date=actor_data.birth_date,
        nationality=actor_data.nationality
    )
    if not actor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Actor with id {actor_id} not found"
        )
    return convert_actor_to_response(actor)


@router.delete("/{actor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    service = ActorService(db)
    success = service.delete_actor(actor_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Actor with id {actor_id} not found"
        )
