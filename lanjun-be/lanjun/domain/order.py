from datetime import datetime
from decimal import Decimal
from typing import Tuple
from uuid import UUID

from pydantic import BaseModel

from lanjun.entities.order import Order


class OrderItem(BaseModel):
    item_id: UUID
    count: int


class OrderModel(BaseModel):
    id: UUID
    user_id: UUID
    cost: Decimal
    created_at: datetime

    items: list[OrderItem]

    @classmethod
    def from_entity(cls, entity: Order, item_counts: list[Tuple[UUID, int]]) -> "OrderModel":
        return cls(
            id=entity.id,
            user_id=entity.user_id,
            cost=entity.cost,
            created_at=entity.created_at,
            items=[OrderItem(item_id=item_id, count=count) for item_id, count in item_counts],
        )
