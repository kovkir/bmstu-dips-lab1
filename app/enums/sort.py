from enum import Enum


class SortPerson(Enum):
    NameAsc  = "name_asc"
    NameDesc = "name_desc"

    AgeAsc  = "age_asc"
    AgeDesc = "age_desc"

    AddressAsc  = "address_asc"
    AddressDesc = "address_desc"

    WorkAsc  = "work_asc"
    WorkDesc = "work_desc"

    IdAsc  = "id_asc"
    IdDesc = "id_desc"
