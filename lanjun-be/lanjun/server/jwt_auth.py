from datetime import datetime, timedelta

from fastapi import Header
from jose import JWTError, jwt

from lanjun.common.settings import JWT_SECRET
from lanjun.domain.user import UserModel
from lanjun.exceptions import AuthorizationException, InvalidJwt


def generate_jwt(user: UserModel) -> str:
    jwt_data = {
        "sub": str(user.id),
        # A month. This is _very_ bad,
        # ideally we want use refresh tokens, but we want to keep it simple
        "exp": datetime.utcnow() + timedelta(hours=720),
        "is_admin": user.is_admin,
    }

    return jwt.encode(jwt_data, JWT_SECRET, algorithm="HS256")


def get_user_id(authorization: str = Header(..., regex="Bearer .*")) -> str:
    token = _get_token_from_header(authorization)
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms="HS256",
            options={
                "require_sub": True,
                "require_exp": True,
            },
        )
    except JWTError as exc:
        raise InvalidJwt(str(exc)) from exc

    user_id: str = payload.get("sub")  # type: ignore
    return user_id


def get_admin_user_id(authorization: str = Header(..., regex="Bearer .*")) -> str:
    token = _get_token_from_header(authorization)
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms="HS256",
            options={
                "require_sub": True,
                "require_exp": True,
            },
        )
    except JWTError as exc:
        raise InvalidJwt(str(exc)) from exc

    is_admin: str = bool(payload.get("is_admin", False))  # type: ignore
    if not is_admin:
        raise AuthorizationException("Admin user needed")

    user_id: str = payload.get("sub")  # type: ignore
    return user_id


def _get_token_from_header(header_value: str) -> str:
    return header_value.split()[1]
