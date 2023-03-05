from lanjun.domain.item import ItemModel
from lanjun.http_models.requests import CreateItem, UpdateItem
from lanjun.http_models.responses import Category, CategoryItems, ItemResponse
from lanjun.repos.item import ItemRepo


async def get_items_per_category() -> CategoryItems:
    result_categories: list[Category] = []
    categories = await ItemRepo.get_categories()

    for category in categories:
        items = await ItemRepo.get_items_in_category(category)
        result_categories.append(
            Category(name=category, items=list(map(ItemResponse.from_model, items)))
        )

    return CategoryItems(categories=result_categories)


async def create_item(item_info: CreateItem) -> ItemModel:
    item = ItemModel.from_item_create_info(item_info)
    await ItemRepo.save(item)
    return item


async def update_item(item_info: UpdateItem) -> None:
    await ItemRepo.update_item(item_info)
