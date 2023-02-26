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
