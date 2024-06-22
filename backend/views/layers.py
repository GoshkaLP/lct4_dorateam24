from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.layer_service import LayerService
from backend.utils.db import get_db
from backend.dto import District, Area, Cadastral, Address

router = APIRouter(prefix="/layers")
layer_service = LayerService()


@router.get(
    "/districts", response_model=list[District], description="Multichoice filter"
)
async def router_get_districts(db: AsyncSession = Depends(get_db)):
    return await layer_service.get_districts(db)


@router.get("/areas", response_model=list[Area], description="Multichoice filter")
async def router_get_areas(db: AsyncSession = Depends(get_db)):
    return await layer_service.get_areas(db)


@router.get(
    "/cadastrals", response_model=list[Cadastral], description="Single choice filter"
)
async def router_get_districts(db: AsyncSession = Depends(get_db)):
    return await layer_service.get_cadastral(db)


@router.get(
    "/addresses", response_model=list[Address], description="Single choice filter"
)
async def router_get_districts(db: AsyncSession = Depends(get_db)):
    return await layer_service.get_addresses(db)
