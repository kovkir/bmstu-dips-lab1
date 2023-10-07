from pydantic import BaseModel, ConfigDict
from fastapi import Query
from typing import Annotated


class PersonBase(BaseModel):
    name: str
    age: Annotated[int | None, Query(ge=1, le=120)] = None
    address: str | None = None
    work: str | None = None


class PersonFilter(BaseModel):
    name: str | None = None
    min_age: Annotated[int | None, Query(ge=1, le=120)] = None
    max_age: Annotated[int | None, Query(ge=1, le=120)] = None
    address: str | None = None
    work: str | None = None


class PersonUpdate(BaseModel):
    name: str | None = None
    age: Annotated[int | None, Query(ge=1, le=120)] = None
    address: str | None = None
    work: str | None = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    # Модели могут быть созданы из экземпляров произвольных классов,
    # прочитав атрибуты экземпляра, соответствующие именам полей моделей. 
    model_config = ConfigDict(from_attributes=True)

    id: int
