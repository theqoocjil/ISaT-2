

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/algorithms", tags=["Work with Algorithms"])


@router.get("/")
async def get_data() -> JSONResponse:
    pass
