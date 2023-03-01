from fastapi import APIRouter, Depends

from lanjun.actions import items as item_actions
from lanjun.http_models.requests import CreateItem
from lanjun.http_models.responses import CategoryItems, ItemResponse
from lanjun.server.jwt_auth import get_admin_user_id

router = APIRouter()


@router.get("/v1/items", response_model=CategoryItems)
async def get_items() -> CategoryItems:
    items = await item_actions.get_items_per_category()
    return items


@router.post("/v1/items", response_model=ItemResponse)
async def create_item(
    item_info: CreateItem, user_id: str = Depends(get_admin_user_id)
) -> ItemResponse:
    item = await item_actions.create_item(item_info)
    return ItemResponse.from_model(item)
