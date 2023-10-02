from models.person import PersonModel
from schemas.person import PersonFilter, PersonUpdate
from enums.sort import SortPerson
from cruds.interfaces import IPersonCRUD


class PersonCRUD(IPersonCRUD):
    async def get_all(
            self, 
            person_filter: PersonFilter,
            sort_field: SortPerson
        ):
        persons = self._db.query(PersonModel)
        persons = await self.__filter_persons(persons, person_filter)
        persons = await self.__sort_persons(persons, sort_field)
    
        return persons.all()

    async def get_by_id(self, person_id: int):
        return self._db.query(PersonModel).filter(PersonModel.id == person_id).first()
    
    async def add(self, person: PersonModel):
        try:
            self._db.add(person)
            self._db.commit()
            self._db.refresh(person)
        except:
            return None
        
        return person
    
    async def delete(self, person: PersonModel):
        self._db.delete(person)
        self._db.commit()
        
        return person

    async def patch(self, person: PersonModel, person_update: PersonUpdate):
        update_fields = person_update.model_dump(exclude_unset=True)        
        for key, value in update_fields.items():
            setattr(person, key, value)
        
        try:
            self._db.add(person)
            self._db.commit()
            self._db.refresh(person)
        except:
            return None
        
        return person

    async def __filter_persons(self, persons, person_filter: PersonFilter):
        if person_filter.name:
            persons = persons.filter(
                PersonModel.name.startswith(person_filter.name))

        if person_filter.min_age:
            persons = persons.filter(
                PersonModel.age >= person_filter.min_age)

        if person_filter.max_age:
            persons = persons.filter(
                PersonModel.age <= person_filter.max_age)

        if person_filter.address:
            persons = persons.filter(
                PersonModel.address.startswith(person_filter.address))
        
        if person_filter.work:
            persons = persons.filter(
                PersonModel.work.startswith(person_filter.work))
        
        return persons
    
    async def __sort_persons(self, persons, sort_field: SortPerson):
        match sort_field:
            case SortPerson.NameAsc:
                persons = persons.order_by(PersonModel.name)
            case SortPerson.NameDesc:
                persons = persons.order_by(PersonModel.name.desc())
            case SortPerson.AgeAsc:
                persons = persons.order_by(PersonModel.age)
            case SortPerson.AgeDesc:
                persons = persons.order_by(PersonModel.age.desc())
            case SortPerson.AddressAsc:
                persons = persons.order_by(PersonModel.address)
            case SortPerson.AddressDesc:
                persons = persons.order_by(PersonModel.address.desc())
            case SortPerson.WorkAsc:
                persons = persons.order_by(PersonModel.work)
            case SortPerson.WorkDesc:
                persons = persons.order_by(PersonModel.work.desc())
            case SortPerson.IdDesc:
                persons = persons.order_by(PersonModel.id.desc())
            case _:
                persons = persons.order_by(PersonModel.id)
        
        return persons
