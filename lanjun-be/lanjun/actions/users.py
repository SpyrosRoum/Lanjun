from typing import Optional
from uuid import UUID

import bcrypt

from lanjun.domain.enums import UserType
from lanjun.domain.user import UserModel
from lanjun.exceptions import NotFoundException
from lanjun.http_models.requests import AuthUser, CreateUser
from lanjun.repos.user import UserRepo


def _hash_password(pwd: str) -> bytes:
    pw = bytes(pwd, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def _check_password(pwd: str, hashed_pwd: str) -> bool:
    pwd_bytes = bytes(pwd, "utf-8")
    hashed_pwd_bytes = bytes(hashed_pwd, "utf-8")
    return bcrypt.checkpw(pwd_bytes, hashed_pwd_bytes)


async def create_user(user: CreateUser, user_type: UserType = UserType.NORMAL) -> UUID:
    hashed_pwd = _hash_password(user.password)
    user_id = await UserRepo.create_new_user(user, hashed_pwd, user_type)
    return user_id


async def login_user(user_auth: AuthUser) -> Optional[UserModel]:
    user = await UserRepo.get_from_email(user_auth.email.lower())
    if user is None:
        return None

    if not _check_password(user_auth.password, user.password):
        return None

    return user


async def get_user_by_id(user_id: UUID) -> Optional[UserModel]:
    return await UserRepo.get(user_id)


async def is_admin(user_id: UUID) -> bool:
    _is_admin = await UserRepo.is_admin(user_id)
    if _is_admin is None:
        raise NotFoundException

    return _is_admin
