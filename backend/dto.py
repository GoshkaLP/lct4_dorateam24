from pydantic import BaseModel


class District(BaseModel):
    id: int
    title: str


class Area(District):
    pass


class Cadastral(District):
    pass


class Address(District):
    pass
