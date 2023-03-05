from decimal import Decimal
from uuid import UUID, uuid4

from httpx import AsyncClient

from lanjun.repos.item import ItemRepo
from lanjun.repos.order import OrderRepo
from lanjun.repos.user import UserRepo


class TestOrders:
    async def test_create_order(
        self, test_client: AsyncClient, user_id: str, jwt_token: str, get_item, get_user
    ):
        user = get_user(id_=UUID(user_id))
        await UserRepo.save(user)

        ids = [uuid4(), uuid4()]
        for id_ in ids:
            item = get_item(id_=id_, price=Decimal("1"))
            await ItemRepo.save(item)

        res = await test_client.post(
            "/v1/orders",
            json={
                "items": [
                    {"item_id": str(ids[0]), "count": 1},
                    {"item_id": str(ids[1]), "count": 1},
                ]
            },
            headers={"Authorization": f"Bearer {jwt_token}"},
        )

        assert res.status_code == 200
        order_id = res.json()["id"]

        order = await OrderRepo.get(order_id)
        assert order is not None
        assert len(order.items) == 2
        assert all(item.item_id in ids for item in order.items)
        assert order.cost == Decimal("2")
