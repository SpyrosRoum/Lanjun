from uuid import UUID

from fastapi import APIRouter, Depends

from lanjun.actions import orders as order_actions
from lanjun.http_models.requests import CreateOrder
from lanjun.http_models.responses import IdResponse
from lanjun.server.jwt_auth import get_user_id

router = APIRouter()


@router.post("/v1/orders", response_model=IdResponse)
async def create_order(order_info: CreateOrder, user_id: str = Depends(get_user_id)) -> IdResponse:
    order_id = await order_actions.create_order(order_info, UUID(user_id))
    return IdResponse(id=order_id)
