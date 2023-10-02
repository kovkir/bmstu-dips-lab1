from sqlalchemy.orm import Session

from models.person import PersonModel
from schemas.person import PersonFilter, PersonUpdate
from enums.sort import SortPerson


class ICRUD():
    def __init__(self, db: Session):
        self._db = db

    async def get_all(
            self, 
            person_filter: PersonFilter,
            sort_field: SortPerson
        ) -> list[PersonModel]:
       pass

    async def get_by_id(self, person_id: int) -> PersonModel | None:
        pass
    
    async def add(self, person: PersonModel) -> PersonModel | None:
        pass
    
    async def delete(self, person: PersonModel) -> PersonModel:
        pass

    async def patch(
            self, 
            person: PersonModel, 
            person_update: PersonUpdate
        ) -> PersonModel | None:
        pass


class IPersonCRUD(ICRUD):
    pass
