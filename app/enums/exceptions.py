from enum import Enum

from schemas.response import HTTPError


class ExcResponses(Enum):
    NotFound = {
        "model": HTTPError,
        "description": "Not Found",
    }
    Conflict = {
        "model": HTTPError,
        "description": "Conflict",
    }
