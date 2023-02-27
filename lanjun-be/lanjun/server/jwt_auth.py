from fastapi import Header
from jose import JWTError, jwt

from lanjun.common.settings import JWT_SECRET
from lanjun.exceptions import InvalidJwt


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


def _get_token_from_header(header_value: str) -> str:
    return header_value.split()[1]
