from fastapi import status
from fastapi.responses import Response

from config.database import DBSessionContext
from cruds.person import PersonCRUD
from models.person import PersonModel
from schemas.person import PersonCreate, PersonFilter, PersonUpdate
from my_exeptions.http_exeptions import NotFoundException, ConflictException
from enums.sort import SortPerson


class PersonServiece(DBSessionContext):
    async def get_all(
            self, 
            person_filter: PersonFilter, 
            sort_field: SortPerson
        ):
        return await PersonCRUD(self.db).get_all(person_filter, sort_field)

    async def get_by_id(self, person_id: int):
        person = await PersonCRUD(self.db).get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Get Person")
        
        return person
    
    async def add(self, person_create: PersonCreate):
        person = PersonModel(**person_create.model_dump())
        person = await PersonCRUD(self.db).add(person)
        if person == None:
            raise ConflictException(prefix="Add Person")
        
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={"Location": f"/api/v1/persons/{person.id}"}
        )
    
    async def delete(self, person_id: int):
        person = await PersonCRUD(self.db).get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Delete Person")
        
        await PersonCRUD(self.db).delete(person)

        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )
    
    async def patch(self, person_id: int, person_update: PersonUpdate):
        person = await PersonCRUD(self.db).get_by_id(person_id)
        if person == None:
            raise NotFoundException(prefix="Update Person")
    
        person = await PersonCRUD(self.db).patch(person, person_update)
        if person == None:
            raise ConflictException(prefix="Update Person")
        
        return person
