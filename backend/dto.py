from pydantic import BaseModel
from typing import Optional


class District(BaseModel):
    id: int
    title: str


class Area(District):
    pass


class Cadastral(District):
    pass


class Address(District):
    pass


class PolygonsRequest(BaseModel):
    districts: Optional[list[str]] = None
    areas: Optional[list[str]] = None
    cadastrals: Optional[list[str]] = None
    addresses: Optional[list[str]] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "districts": ["НАО"],
                    "areas": ["Сельское поселение Воскресенское"],
                    "cadastrals": ["50:21:0130304:57"],
                    "addresses": [
                        "(Местоположение установлено относительно ориентира, расположенного в границах участка. Почтовый адрес ориентира: город Москва, поселение"
                    ],
                }
            ]
        }
    }


class Feature(BaseModel):
    type: str = "Feature"
    properties: dict
    geometry: dict


class FeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: list[Feature]


class AuthForm(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token: str


class TokenData(BaseModel):
    id: int
    email: str
