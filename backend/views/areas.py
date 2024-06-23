from fastapi import APIRouter, Depends, Security
from asyncpg import Connection
from backend.dto import PolygonsRequest, FeatureCollection, SearchHistory
from backend.utils.db import get_db
from backend.services.areas_service import AreasService
from backend.dependencies.token import token_utility


router = APIRouter(tags=["Area polygons"], prefix="/polygons")
areas_service = AreasService()


@router.post(
    "/",
    response_model=FeatureCollection,
    # dependencies=[Security(token_utility)]
)
async def get_areas_by_navigation_filters(
    request_data: PolygonsRequest, db: Connection = Depends(get_db)
):
    response = await areas_service.get_polygons(db=db, request_data=request_data)
    return FeatureCollection.model_validate({"features": response})


@router.get("/search/history", response_model=list[SearchHistory])
async def areas_search_history(user_id: int, db: Connection = Depends(get_db)):
    response = await areas_service.get_search_history(db=db, user_id=user_id)
    return response
