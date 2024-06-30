from pydantic import BaseModel
from datetime import datetime
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


class RectangleSearch(BaseModel):
    lonMin: float
    latMin: float
    lonMax: float
    latMax: float


class RadiusSearch(BaseModel):
    radius: float
    lon: float
    lat: float


class PolygonsRequest(BaseModel):
    districts: Optional[list[str]] = None
    areas: Optional[list[str]] = None
    cadastrals: Optional[list[str]] = None
    addresses: Optional[list[str]] = None
    crossingFilters: Optional[dict[str, int]] = None
    rectangleSearch: Optional[RectangleSearch] = None
    radiusSearch: Optional[RadiusSearch] = None

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
                    "crossingFilters": {"is_zpo": 0, "is_msk": 1},
                    "rectangelSearch": {
                        "lonMin": 37.189182,
                        "latMin": 55.5915758,
                        "lonMax": 37.5558507,
                        "latMax": 55.722506,
                    },
                    "radiusSearch": {
                        "lon": 37.2161114,
                        "lat": 55.5853671,
                        "radius": 1000,
                    },
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


class CrossingTerritories(BaseModel):
    id: int
    title: str
    description: str
    key: str


class SearchHistory(BaseModel):
    id: int
    user_id: int
    search_request: str
    date_created: datetime
