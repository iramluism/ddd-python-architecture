

from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
async def heathcheck():
    # TODO check database connection, make ping to thirty APIs
    return "HEALTHY"
