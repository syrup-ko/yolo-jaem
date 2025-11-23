from typing import Dict


async def get_user_profile(user_id: str) -> Dict:
    return {"id": user_id, "email": f"{user_id}@example.com"}



