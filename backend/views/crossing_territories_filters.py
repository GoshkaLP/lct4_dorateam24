from asyncpg import Connection
from fastapi import APIRouter, Depends, Security
from backend.utils.db import get_db
from backend.dependencies.token import token_utility
from backend.dto import CrossingTerritories
from backend.services.layer_service import LayerService


router = APIRouter(tags=["Crossing territories filters"], prefix="/crossing/filters")
layer_service = LayerService()


@router.get(
    "/",
    response_model=list[CrossingTerritories],
    summary="Пересечения территорий",
    # dependencies=[Security(token_utility)],
)
async def router_get_crossing_territories(db: Connection = Depends(get_db)):
    return await layer_service.get_crossing_territories_filters(db=db)
