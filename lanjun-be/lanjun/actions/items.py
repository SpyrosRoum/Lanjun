from lanjun.http_models.responses import CategoryItems, ItemResponse, Category
from lanjun.repos.item import ItemRepo


async def get_items_per_category() -> CategoryItems:
    result_categories: list[Category] = []
    categories = await ItemRepo.get_categories()

    for category in categories:
        items = await ItemRepo.get_items_in_category(category)
        items = map(ItemResponse.from_model, items)
        result_categories.append(Category(name=category, items=items))

    return CategoryItems(categories=result_categories)
