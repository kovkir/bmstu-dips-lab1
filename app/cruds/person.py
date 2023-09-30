from config.database import DBSessionContext
from models.person import PersonModel
from schemas.person import PersonFilter, PersonUpdate
from enums.sort import SortPerson


class PersonCRUD(DBSessionContext):
    async def get_all(
            self, 
            person_filter: PersonFilter,
            sort_field: SortPerson, 
            skip: int = 0, limit: int = 100
        ):
        persons = self.db.query(PersonModel)
        persons = await self.__filter_persons(persons, person_filter)
        persons = await self.__sort_persons(persons, sort_field)
    
        return persons.offset(skip).limit(limit).all()

    async def get_by_id(self, person_id: int):
        return self.db.query(PersonModel).filter(PersonModel.id == person_id).first()
    
    async def add(self, person: PersonModel):
        try:
            self.db.add(person)
            self.db.commit()
            self.db.refresh(person)
        except:
            return None
        
        return person
    
    async def delete(self, person: PersonModel):
        self.db.delete(person)
        self.db.commit()
        
        return person

    async def patch(self, person: PersonModel, person_update: PersonUpdate):
        update_fields = person_update.model_dump(exclude_unset=True)        
        for key, value in update_fields.items():
            setattr(person, key, value)
        
        try:
            self.db.add(person)
            self.db.commit()
            self.db.refresh(person)
        except:
            return None
        
        return person

    async def __filter_persons(self, persons, person_filter: PersonFilter):
        if person_filter.first_name:
            persons = persons.filter(
                PersonModel.first_name.startswith(person_filter.first_name))
        if person_filter.last_name:
            persons = persons.filter(
                PersonModel.last_name.startswith(person_filter.last_name))
        if person_filter.min_birth_year:
            persons = persons.filter(
                PersonModel.birth_year >= person_filter.min_birth_year)
        if person_filter.max_birth_year:
            persons = persons.filter(
                PersonModel.birth_year <= person_filter.max_birth_year)
        if person_filter.email:
            persons = persons.filter(
                PersonModel.email == person_filter.email)
        if person_filter.is_man != None:
            persons = persons.filter(
                PersonModel.is_man == person_filter.is_man)
        
        return persons
    
    async def __sort_persons(self, persons, sort_field: SortPerson):
        match sort_field:
            case SortPerson.FirstNameAsc:
                persons = persons.order_by(PersonModel.first_name)
            case SortPerson.FirstNameDesc:
                persons = persons.order_by(PersonModel.first_name.desc())
            case SortPerson.LastNameAsc:
                persons = persons.order_by(PersonModel.last_name)
            case SortPerson.LastNameDesc:
                persons = persons.order_by(PersonModel.last_name.desc())
            case SortPerson.BirthYearAsc:
                persons = persons.order_by(PersonModel.birth_year)
            case SortPerson.BirthYearDesc:
                persons = persons.order_by(PersonModel.birth_year.desc())
            case SortPerson.EmailAsc:
                persons = persons.order_by(PersonModel.email)
            case SortPerson.EmailDesc:
                persons = persons.order_by(PersonModel.email.desc())
            case SortPerson.IsManAsc:
                persons = persons.order_by(PersonModel.is_man)
            case SortPerson.IsManDesc:
                persons = persons.order_by(PersonModel.is_man.desc())
            case SortPerson.IdDesc:
                persons = persons.order_by(PersonModel.id.desc())
            case _:
                persons = persons.order_by(PersonModel.id)
        
        return persons
    