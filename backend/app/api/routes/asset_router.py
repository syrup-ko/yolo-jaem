from fastapi import APIRouter

router = APIRouter()


@router.get("/assets")
async def list_assets():
    return {"assets": ["Stock", "HYSA", "RealEstate"]}



