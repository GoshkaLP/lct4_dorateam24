from fastapi import APIRouter


router = APIRouter(prefix="/api")


@router.get("/debug")
def debug():
    return "ok"
