from sqlalchemy.orm import Session

from models.person import PersonModel
from schemas.person import PersonCreate, PersonFilter, PersonUpdate
from my_exceptions.http_exceptions import NotFoundException, ConflictException
from enums.sort import SortPerson
from cruds.interfaces.person import IPersonCRUD


class PersonService():
    def __init__(self, personCRUD: type[IPersonCRUD], db: Session):
        self._personCRUD = personCRUD(db)
        
    async def get_all(
            self,
            person_filter: PersonFilter, 
            sort_field: SortPerson
        ):
        return await self._personCRUD.get_all(person_filter, sort_field)

    async def get_by_id(self, person_id: int):
        person = await self._personCRUD.get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Get Person")
        
        return person
    
    async def add(self, person_create: PersonCreate):
        person = PersonModel(**person_create.model_dump())
        person = await self._personCRUD.add(person)
        if person == None:
            raise ConflictException(prefix="Add Person")
        
        return person
    
    async def delete(self, person_id: int):
        person = await self._personCRUD.get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Delete Person")
        
        return await self._personCRUD.delete(person)
    
    async def patch(self, person_id: int, person_update: PersonUpdate):
        person = await self._personCRUD.get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Update Person")
    
        person = await self._personCRUD.patch(person, person_update)
        if person == None:
            raise ConflictException(prefix="Update Person")
        
        return person
