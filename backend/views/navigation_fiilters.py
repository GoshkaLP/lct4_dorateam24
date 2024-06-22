from fastapi import APIRouter, Depends
from asyncpg import Connection
from backend.services.layer_service import LayerService
from backend.utils.db import get_db
from backend.dto import District, Area, Cadastral, Address

router = APIRouter(tags=["Navigation filters"], prefix="/navigation/filters")
layer_service = LayerService()


@router.get(
    "/districts",
    response_model=list[District],
    description="Multichoice filter",
    summary="Муниципальные округа",
)
async def router_get_districts(db: Connection = Depends(get_db)):
    return await layer_service.get_districts(db)


@router.get(
    "/areas",
    response_model=list[Area],
    description="Multichoice filter",
    summary="Районы",
)
async def router_get_areas(db: Connection = Depends(get_db)):
    return await layer_service.get_areas(db)


@router.get(
    "/cadastrals",
    response_model=list[Cadastral],
    description="Multichoice filter",
    summary="Кадастровые номера",
)
async def router_get_districts(db: Connection = Depends(get_db)):
    return await layer_service.get_cadastrals(db)


@router.get(
    "/addresses",
    response_model=list[Address],
    description="Multichoice filter",
    summary="Адреса",
)
async def router_get_districts(db: Connection = Depends(get_db)):
    return await layer_service.get_addresses(db)
