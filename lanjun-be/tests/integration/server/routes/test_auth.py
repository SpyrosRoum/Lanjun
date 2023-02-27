from collections.abc import Callable
from random import randint
from typing import Optional
from uuid import uuid4

import pytest
from httpx import AsyncClient

from lanjun.http_models.requests import CreateUser
from lanjun.http_models.responses import LoginToken, UserCreated
from lanjun.repos.user import UserRepo


@pytest.fixture(scope="function")
def get_create_user() -> Callable[[], CreateUser]:
    def _wrapper(
        email: Optional[str] = None,
        name: str = "Name Surname",
        password: str = "12345",
        address: Optional[str] = None,
        floor: Optional[str] = None,
        bell: Optional[str] = None,
        phone: str = str(randint(690_000, 699_999)),
    ) -> CreateUser:
        return CreateUser(
            email=email or f"{str(uuid4())}@mail.com",
            name=name,
            password=password,
            address=address,
            floor=floor,
            bell=bell,
            phone=phone,
        )

    return _wrapper


class TestSignUp:
    async def test_signup_creates_user(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(email="foo@mail.com")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())

        assert res.status_code == 201

        user_created = UserCreated.validate(res.json())

        user = await UserRepo.get(user_created.id)
        assert user is not None
        assert user.email == "foo@mail.com"

    async def test_duplicate_mail(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(email="foo@mail.com")
        await test_client.post("/v1/sign_up", json=create_user.dict())
        create_user = get_create_user(email="foo@mail.com")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())

        assert res.status_code == 400

    async def test_duplicate_phone(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(phone="1234")
        await test_client.post("/v1/sign_up", json=create_user.dict())
        create_user = get_create_user(phone="1234")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())

        assert res.status_code == 400


class TestLogin:
    async def test_login(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(email="foo@mail.com", password="12345")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())
        assert res.status_code == 201

        res = await test_client.post(
            "/v1/login", json={"email": "foo@mail.com", "password": "12345"}
        )
        assert res.status_code == 200
        LoginToken.validate(res.json())

    async def test_login_wrong_pwd(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(email="foo@mail.com", password="12345")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())
        assert res.status_code == 201

        res = await test_client.post(
            "/v1/login", json={"email": "foo@mail.com", "password": "WRONG"}
        )
        assert res.status_code == 401

    async def test_login_wrong_email(self, test_client: AsyncClient, get_create_user):
        create_user = get_create_user(email="foo@mail.com", password="12345")
        res = await test_client.post("/v1/sign_up", json=create_user.dict())
        assert res.status_code == 201

        res = await test_client.post(
            "/v1/login", json={"email": "WRONG@mail.com", "password": "12345"}
        )
        assert res.status_code == 401
