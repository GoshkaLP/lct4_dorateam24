from backend.views.navigation_fiilters import router as navigation_filters_router
from backend.views.areas import router as areas_router
from backend.views.auth import router as auth_router
from backend.views.crossing_territories_filters import (
    router as crossing_territories_filters_router,
)

routers = [
    auth_router,
    navigation_filters_router,
    crossing_territories_filters_router,
    areas_router,
]
