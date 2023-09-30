from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi import Query
from typing import Annotated


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_year: Annotated[int | None, Query(gt=1900, lt=2023)]
    email: EmailStr | None = None
    is_man: bool


class PersonFilter(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    min_birth_year: Annotated[int | None, Query(gt=1900, lt=2023)] = None,
    max_birth_year: Annotated[int | None, Query(gt=1900, lt=2023)] = None,
    email: EmailStr | None = None
    is_man: bool | None = None


class PersonUpdate(BaseModel):
    email: EmailStr | None = None
    last_name: str = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    # Модели могут быть созданы из экземпляров произвольных классов,
    # прочитав атрибуты экземпляра, соответствующие именам полей моделей. 
    model_config = ConfigDict(from_attributes=True)

    id: int
