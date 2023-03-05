from decimal import Decimal

from httpx import AsyncClient

from lanjun.domain.item import ItemModel
from lanjun.http_models.requests import CreateItem
from lanjun.http_models.responses import ItemResponse
from lanjun.repos.item import ItemRepo


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

    async def test_update_item(self, test_client: AsyncClient, admin_jwt_token: str, get_item):
        item = get_item()
        await ItemRepo.save(item)

        resp = await test_client.put(
            "/v1/items",
            json={
                "id": str(item.id),
                "name": "New name",
                "image_url": item.image_url,
                "description": item.description,
                "category": item.category,
                "price": str(item.price),
            },
            headers={"Authorization": f"Bearer {admin_jwt_token}"},
        )

        assert resp.status_code == 200

        updated_item = await ItemRepo.get(item.id)

        assert updated_item.name == "New name"
        assert updated_item.image_url == item.image_url
        assert updated_item.description == item.description
        assert updated_item.category == item.category
        assert updated_item.price == item.price

    async def test_update_item_doesnt_exist(
        self, test_client: AsyncClient, admin_jwt_token: str, get_item
    ):
        item = get_item()

        resp = await test_client.put(
            "/v1/items",
            json={
                "id": str(item.id),
                "name": "New name",
                "image_url": item.image_url,
                "description": item.description,
                "category": item.category,
                "price": str(item.price),
            },
            headers={"Authorization": f"Bearer {admin_jwt_token}"},
        )

        assert resp.status_code == 404
        assert resp.json() == {"detail": "Item not found"}
