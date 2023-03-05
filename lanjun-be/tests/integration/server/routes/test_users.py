from httpx import AsyncClient

from lanjun.http_models.requests import CreateUser
from lanjun.http_models.responses import UserResponse


class testUsers:
    async def test_user_flow(self, test_client: AsyncClient, admin_jwt_token: str):
        user_info = CreateUser(
            email="test@test.com", name="Name", password="pass", phone="1234566"
        )
        resp = await test_client.post("/v1/sign_up", json=user_info.json())
        assert resp.status_code == 201

        resp = await test_client.post(
            "/v1/login", json={"email": "test@test.com", "password": "pass"}
        )
        assert resp.status_code == 200

        token = resp.json()["token"]

        resp = await test_client.get("/v1/users/me", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 200

        user = UserResponse.validate(resp.json())

        assert user.email == user_info.email
        assert user.name == user_info.name
        assert user.phone == user_info.phone
