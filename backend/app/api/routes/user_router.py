from fastapi import APIRouter, Depends
from ...core.security import get_current_user

router = APIRouter()


@router.get("/user/me")
async def get_me(user_id: str = Depends(get_current_user)):
    return {"id": user_id, "email": f"{user_id}@example.com"}



