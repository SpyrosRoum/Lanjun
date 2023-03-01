from decimal import Decimal

from lanjun.actions import items as item_actions
from lanjun.http_models.requests import CreateItem
from lanjun.repos.item import ItemRepo


class TestItemActions:
    async def test_create_item(self):
        item_info = CreateItem(
            name="Item Name",
            image_url="url",
            description="descr",
            category="a",
            price=Decimal("3.14"),
        )

        await item_actions.create_item(item_info)

        items_in_db = await ItemRepo.get_items_in_category("a")

        assert len(items_in_db) == 1

        item = items_in_db[0]
        assert item.name == "Item Name"
        assert item.description == "descr"
        assert item.image_url == "url"
        assert item.price == Decimal("3.14")
