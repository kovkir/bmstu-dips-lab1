from models.person import PersonModel
from schemas.person import PersonFilter, PersonUpdate
from enums.sort import SortPerson
from cruds.interfaces.person import IPersonCRUD
from mocks.data import PersonDataMock


class PersonMockCRUD(IPersonCRUD, PersonDataMock):
    async def get_all(
            self, 
            person_filter: PersonFilter,
            sort_field: SortPerson
        ) -> list[PersonModel]:
        persons = [
            PersonModel(**item) for item in self._persons
        ]
        persons = await self.__filter_persons(persons, person_filter)
        persons = await self.__sort_persons(persons, sort_field)
    
        return persons

    async def get_by_id(self, person_id: int) -> PersonModel | None:
        for item in self._persons:
            if item["id"] == person_id:
                return PersonModel(**item)
            
        return None
    
    async def add(self, person: PersonModel) -> PersonModel | None:
        for item in self._persons:
            if item["name"] == person.name:
                return None
            if item.get("address") != None and \
               item.get("address") == person.address:
                return None
            
        self._persons.append(
            {
                "id": 1 if len(self._persons) else self._persons[-1].id + 1,
                "name": person.name,
                "age": person.age,
                "address": person.address,
                "work": person.work
            },
        )
        
        return PersonModel(**self._persons[-1])
    
    async def delete(self, person: PersonModel) -> PersonModel:
        for i in range(len(self._persons)):
            item = self._persons[i]
            if item["id"] == person.id:
                deleted_person = self._persons.pop(i)
                break
                
        return deleted_person

    async def patch(
            self, 
            person: PersonModel, 
            person_update: PersonUpdate
        ) -> PersonModel | None:
            
        for item in self._persons:
            if item["id"] != person.id:
                if item["name"] == person.name:
                    return None
                if item.get("address") != None and \
                   item.get("address") == person.address:
                    return None
        
        update_fields = person_update.model_dump(exclude_unset=True) 
        for item in self._persons:
            if item["id"] == person.id:
                for key in update_fields:
                    item[key] = update_fields[key]

                updated_person = PersonModel(**item)
                break

        return updated_person

    async def __filter_persons(self, persons, person_filter: PersonFilter):
        return persons
    
    async def __sort_persons(self, persons, sort_field: SortPerson):
        return persons
