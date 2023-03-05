from uuid import UUID

from fastapi import APIRouter, Depends

from lanjun.actions import items as item_actions
from lanjun.http_models.requests import CreateItem, UpdateItem
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


@router.put("/v1/items")
async def update_item(item_info: UpdateItem, user_id: str = Depends(get_admin_user_id)) -> None:
    await item_actions.update_item(item_info)


@router.delete("/v1/items/{item_id}")
async def delete_item(item_id: UUID, user_id: str = Depends(get_admin_user_id)) -> None:
    await item_actions.delete_item(item_id)
