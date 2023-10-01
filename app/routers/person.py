from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import Annotated

from schemas.person import PersonFilter, PersonCreate, PersonUpdate
from services.person import PersonServiece
from enums.responses import RespEnum
from enums.sort import SortPerson
from config.database import get_db


router = APIRouter(
    prefix="/persons",
    tags=["Person REST API operations"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespEnum.InvalidData.value,
    }
)


@router.get(
    "/", 
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: RespEnum.GetAll.value,
    }
)
async def get_all_persons(
        db: Annotated[Session, Depends(get_db)],
        name: str | None = None,
        min_age: Annotated[int | None, Query(ge=1, le=120)] = None,
        max_age: Annotated[int | None, Query(ge=1, le=120)] = None,
        address: str | None = None,
        work: str | None = None,
        sort_field: SortPerson = SortPerson.IdAsc
    ):
    return await PersonServiece(db).get_all(
        person_filter=PersonFilter(
            name=name,
            min_age=min_age,
            max_age=max_age,
            address=address,
            work=work
        ),
        sort_field=sort_field
    )


@router.get(
    "/{person_id}/", 
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: RespEnum.GetByID.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
    }
)
async def get_person_by_id(
        db: Annotated[Session, Depends(get_db)],
        person_id: int
    ):
    return await PersonServiece(db).get_by_id(person_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        status.HTTP_201_CREATED: RespEnum.Created.value,
        status.HTTP_409_CONFLICT: RespEnum.Conflict.value,
    }
)
async def create_new_person(
        db: Annotated[Session, Depends(get_db)], 
        person_create: PersonCreate
    ):
    return await PersonServiece(db).add(person_create)


@router.delete(
    "/{person_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_204_NO_CONTENT: RespEnum.Delete.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
    }
)
async def remove_person_by_id(
        db: Annotated[Session, Depends(get_db)], 
        person_id: int
    ):
    return await PersonServiece(db).delete(person_id)


@router.patch(
    "/{person_id}/",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: RespEnum.Patch.value,
        status.HTTP_404_NOT_FOUND: RespEnum.NotFound.value,
        status.HTTP_409_CONFLICT: RespEnum.Conflict.value,
    }
)
async def update_person_by_id(
        db: Annotated[Session, Depends(get_db)], 
        person_id: int,
        person_update: PersonUpdate
    ):
    return await PersonServiece(db).patch(person_id, person_update)
