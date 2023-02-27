from fastapi import APIRouter, status

import lanjun.actions.users as user_actions
from lanjun.exceptions import InvalidCredentials
from lanjun.http_models.requests import AuthUser, CreateUser
from lanjun.http_models.responses import LoginToken, UserCreated
from lanjun.server.jwt_auth import generate_jwt

router = APIRouter()


@router.post("/v1/sign_up", status_code=status.HTTP_201_CREATED, response_model=UserCreated)
async def sign_up(user: CreateUser) -> UserCreated:
    user_id = await user_actions.create_user(user)
    return UserCreated(id=user_id)


@router.post("/v1/login", response_model=LoginToken)
async def login(auth_user: AuthUser) -> LoginToken:
    user = await user_actions.login_user(auth_user)
    if user is None:
        raise InvalidCredentials()

    return LoginToken(token=generate_jwt(user))
