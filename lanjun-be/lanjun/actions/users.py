from uuid import UUID

import bcrypt

from lanjun.http_models.requests import CreateUser
from lanjun.repos.user import UserRepo


def _hash_password(pwd: str) -> bytes:
    pw = bytes(pwd, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


async def create_user(user: CreateUser) -> UUID:
    hashed_pwd = _hash_password(user.password)
    user_id = await UserRepo.create_new_user(user, hashed_pwd)
    return user_id
