from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Annotated

from schemas.person import Person, PersonFilter, PersonCreate, PersonUpdate
from schemas.response import EmptyBody
from services.person import PersonServiece
from enums.exceptions import ExcResponses
from enums.sort import SortPerson
from config.database import get_db


router = APIRouter(
    prefix="/persons",
    tags=["Person"]
)


@router.get(
    "/", 
    status_code=status.HTTP_200_OK,
    response_model=list[Person]
)
async def get_all(
        db: Annotated[Session, Depends(get_db)],
        first_name: str | None = None,
        last_name: str | None = None,
        min_birth_year: Annotated[int | None, Query(gt=1900, lt=2023)] = None,
        max_birth_year: Annotated[int | None, Query(gt=1900, lt=2023)] = None,
        email: str | None = None,
        phone_number: str | None = None,
        is_man: bool | None = None,
        sort_field: SortPerson = SortPerson.IdAsc
    ):
    persons = await PersonServiece(db).get_all(
        person_filter=PersonFilter(
            first_name=first_name,
            last_name=last_name,
            min_birth_year=min_birth_year,
            max_birth_year=max_birth_year,
            email=email,
            phone_number=phone_number,
            is_man=is_man
        ),
        sort_field=sort_field
        )
    return persons


@router.get(
    "/{person_id}/", 
    status_code=status.HTTP_200_OK,
    response_model=Person,
    responses={
        status.HTTP_404_NOT_FOUND: ExcResponses.NotFound.value,
    }
)
async def get_by_id(
        db: Annotated[Session, Depends(get_db)],
        person_id: int
    ):
    return await PersonServiece(db).get_by_id(person_id)


@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED,
    response_model=EmptyBody,
    responses={
        status.HTTP_409_CONFLICT: ExcResponses.Conflict.value,
    }
)
async def add(
        db: Annotated[Session, Depends(get_db)], 
        person_create: PersonCreate
    ):
    return await PersonServiece(db).add(person_create)


@router.delete(
    "/{person_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Person,
    responses={
        status.HTTP_404_NOT_FOUND: ExcResponses.NotFound.value,
    }
)
async def delete(
        db: Annotated[Session, Depends(get_db)], 
        person_id: int
    ):
    return await PersonServiece(db).delete(person_id)


@router.patch(
    "/{person_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Person,
    responses={
        status.HTTP_404_NOT_FOUND: ExcResponses.NotFound.value,
        status.HTTP_409_CONFLICT: ExcResponses.Conflict.value,
    }
)
async def Patch(
        db: Annotated[Session, Depends(get_db)], 
        person_id: int,
        person_update: PersonUpdate
    ):
    return await PersonServiece(db).patch(person_id, person_update)
