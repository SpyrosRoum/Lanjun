from uuid import UUID

from fastapi import APIRouter, Depends

from lanjun.actions import orders as order_actions
from lanjun.actions import users as user_actions
from lanjun.http_models.requests import CreateOrder
from lanjun.http_models.responses import IdResponse, Orders
from lanjun.server.jwt_auth import get_user_id, get_admin_user_id

router = APIRouter()


@router.post("/v1/orders", response_model=IdResponse)
async def create_order(order_info: CreateOrder, user_id: str = Depends(get_user_id)) -> IdResponse:
    order_id = await order_actions.create_order(order_info, UUID(user_id))
    return IdResponse(id=order_id)


@router.get("/v1/orders", response_model=Orders)
async def get_orders(user_id: str = Depends(get_user_id)) -> Orders:
    if await user_actions.is_admin(UUID(user_id)):
        orders = await order_actions.get_all_orders()
    else:
        orders = await order_actions.get_orders_for_user(UUID(user_id))

    return Orders(orders=orders)


@router.delete("/v1/orders/{order_id}")
async def delete_orders(order_id: UUID, user_id: str = Depends(get_admin_user_id)) -> None:
    await order_actions.delete_order(order_id)
