from collections.abc import Callable
from datetime import datetime, timedelta
from typing import Any

import pytest
from jose import jwt

from lanjun.common.settings import JWT_SECRET


@pytest.fixture(scope="function")
def user_id() -> str:
    return "4567f71d-6c87-4cb1-8766-3092b9d6f7c2"


@pytest.fixture(scope="function")
def jwt_token(user_id: str, generate_jwt_token: Callable[[dict[str, Any]], str]) -> str:
    tomorrow_timestamp = datetime.now() + timedelta(days=1)
    payload = {"sub": user_id, "exp": tomorrow_timestamp, "is_admin": False}
    token = generate_jwt_token(payload)

    return token


@pytest.fixture(scope="function")
def admin_jwt_token(user_id: str, generate_jwt_token: Callable[[dict[str, Any]], str]) -> str:
    tomorrow_timestamp = datetime.now() + timedelta(days=1)
    payload = {"sub": user_id, "exp": tomorrow_timestamp, "is_admin": True}
    token = generate_jwt_token(payload)

    return token


@pytest.fixture
def generate_jwt_token() -> Callable[[dict[str, Any]], str]:
    def _generate_jwt_token(payload: dict[str, Any]) -> str:
        return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return _generate_jwt_token
