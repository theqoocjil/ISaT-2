
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.data import DataService


router = APIRouter(prefix="/data", tags=["Work with Data"])


@router.put("/")
async def get_data() -> JSONResponse:
    d = DataService()
    d.add_friends()
    return True
