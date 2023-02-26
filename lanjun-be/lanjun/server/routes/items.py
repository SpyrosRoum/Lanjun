from fastapi import APIRouter

from lanjun.actions import items as item_actions
from lanjun.http_models.responses import CategoryItems

router = APIRouter()


@router.get("/v1/items", response_model=CategoryItems)
async def get_items() -> CategoryItems:
    items = await item_actions.get_items_per_category()
    return items
