from pydantic import BaseModel


class Create(BaseModel):
    filters: dict
    params: dict
    base: str | None = None


class Get(BaseModel):
    filters: dict
    base: str | None = None


class Update(BaseModel):
    filters: dict
    params: dict
    base: str | None = None
