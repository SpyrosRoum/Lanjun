from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from lanjun.actions import items as item_actions
from lanjun.domain.order import OrderModel
from lanjun.exceptions import NotFoundException
from lanjun.http_models.requests import CreateOrder
from lanjun.repos.order import OrderRepo


async def create_order(order_info: CreateOrder, user_id: UUID) -> UUID:
    cost = Decimal("0")
    for item in order_info.items:
        item_cost = await item_actions.get_item_cost(item.item_id)
        if item_cost is None:
            raise NotFoundException("One or more items don't exist")
        cost += item_cost

    order = OrderModel(
        id=uuid4(),
        user_id=user_id,
        cost=cost,
        created_at=datetime.utcnow(),
        items=order_info.items,
    )

    await OrderRepo.save(order)

    return order.id
