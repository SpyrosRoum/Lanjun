from fastapi import APIRouter, status

import lanjun.actions.users as user_actions
from lanjun.http_models.requests import CreateUser
from lanjun.http_models.responses import UserCreated

router = APIRouter()


@router.post("/v1/sign_up", status_code=status.HTTP_201_CREATED, response_model=UserCreated)
async def sign_up(user: CreateUser) -> UserCreated:
    user_id = await user_actions.create_user(user)
    return UserCreated(id=user_id)


@router.post("/login")
async def login() -> None:
    pass
