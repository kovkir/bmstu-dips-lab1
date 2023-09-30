from pydantic import BaseModel, ConfigDict


class HTTPError(BaseModel):
    detail: str

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {"detail": "Method: exception description"},
        }
    )


class EmptyBody(BaseModel):
    model_config = ConfigDict(
        json_schema_extra = {
            "example": "null",
        }
    )
