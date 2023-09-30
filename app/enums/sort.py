from enum import Enum


class SortPerson(Enum):
    FirstNameAsc  = "first_name_asc"
    FirstNameDesc = "first_name_desc"

    LastNameAsc  = "last_name_asc"
    LastNameDesc = "last_name_desc"

    BirthYearAsc  = "birth_year_asc"
    BirthYearDesc = "birth_year_desc"

    EmailAsc  = "email_asc"
    EmailDesc = "email_desc"

    IsManAsc  = "is_man_asc"
    IsManDesc = "is_man_desc"

    IdAsc  = "id_asc"
    IdDesc = "id_desc"
