from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends

from lanjun.actions.users import get_user_by_id
from lanjun.http_models.responses import UserResponse
from lanjun.server.jwt_auth import get_user_id

router = APIRouter()


@router.get("/v1/users/me", response_model=UserResponse)
async def get_me(user_id: str = Depends(get_user_id)) -> Optional[UserResponse]:
    user = await get_user_by_id(UUID(user_id))
    if user is None:
        return None

    return UserResponse.from_model(user)
