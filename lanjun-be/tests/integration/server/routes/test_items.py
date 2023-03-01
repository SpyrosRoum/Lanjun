from decimal import Decimal

from httpx import AsyncClient

from lanjun.domain.item import ItemModel
from lanjun.http_models.requests import CreateItem
from lanjun.http_models.responses import ItemResponse


class TestItemEndpoints:
    async def test_create_item(self, test_client: AsyncClient, admin_jwt_token: str):
        resp = await test_client.post(
            "/v1/items",
            json={
                "name": "Item Name",
                "image_url": "url",
                "description": "descr",
                "category": "a",
                "price": "3.14",
            },
            headers={"Authorization": f"Bearer {admin_jwt_token}"},
        )

        assert resp.status_code == 200
        item = ItemResponse.validate(resp.json())

        assert item.name == "Item Name"
        assert item.image == "url"
        assert item.description == "descr"

    async def test_create_item_no_admin(self, test_client: AsyncClient, jwt_token: str):
        item_info = CreateItem(
            name="Item Name",
            image_url="url",
            description="descr",
            category="a",
            price=Decimal("3.14"),
        )

        resp = await test_client.post(
            "/v1/items",
            json=item_info.json(),
            headers={"Authorization": f"Bearer {jwt_token}"},
        )

        assert resp.status_code == 401
