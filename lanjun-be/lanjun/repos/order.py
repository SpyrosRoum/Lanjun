import logging
from typing import Optional
from uuid import UUID

from sqlalchemy import select

from lanjun.database import db_session
from lanjun.domain.order import OrderModel
from lanjun.entities.links import OrderItemLink
from lanjun.entities.order import Order

logger = logging.getLogger(__name__)


class OrderRepo:
    @classmethod
    async def save(cls, order: OrderModel) -> None:
        entity = Order(
            id=order.id, user_id=order.user_id, cost=order.cost, created_at=order.created_at
        )
        async with db_session() as session:
            session.add(entity)

            await session.commit()

            for item in order.items:
                link_entity = OrderItemLink(
                    order_id=order.id,
                    item_id=item.item_id,
                    item_count=item.count,
                )
                session.add(link_entity)

            await session.commit()

    @classmethod
    async def get(cls, order_id: UUID) -> Optional[OrderModel]:
        query = select(Order).where(Order.id == order_id)

        async with db_session() as session:
            res = await session.execute(query)
            entity: Optional[Order] = res.scalar_one_or_none()

            if entity is None:
                return None

            query = select(OrderItemLink.item_id).where(OrderItemLink.order_id == order_id)
            res = await session.execute(query)
            item_ids = res.scalars().all()

            order_items = []
            for item_id in item_ids:
                query = (
                    select(OrderItemLink.item_count)
                    .where(OrderItemLink.order_id == order_id)
                    .where(OrderItemLink.item_id == item_id)
                )
                res = await session.execute(query)
                count = res.scalar_one_or_none()
                order_items.append((item_id, count))

            return OrderModel.from_entity(entity, order_items)

    @classmethod
    async def get_orders_for_user(cls, user_id: UUID) -> list[OrderModel]:
        query = select(Order.id).where(Order.user_id == user_id)

        async with db_session() as session:
            res = await session.execute(query)
            order_ids = res.scalars().all()

        orders = []
        for order_id in order_ids:
            order = await cls.get(order_id)
            orders.append(order)

        return orders

    @classmethod
    async def get_all_orders(cls) -> list[OrderModel]:
        query = select(Order.id)

        async with db_session() as session:
            res = await session.execute(query)
            order_ids = res.scalars().all()

        orders = []
        for order_id in order_ids:
            order = await cls.get(order_id)
            orders.append(order)

        return orders
