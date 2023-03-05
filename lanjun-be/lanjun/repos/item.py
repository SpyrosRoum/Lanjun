import logging
from typing import Optional
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError

from lanjun.database import db_session
from lanjun.domain.item import ItemModel
from lanjun.entities.item import Item
from lanjun.exceptions import NotFoundException
from lanjun.http_models.requests import UpdateItem

logger = logging.getLogger(__name__)


class ItemRepo:
    @classmethod
    async def save(cls, item: ItemModel) -> None:
        entity = Item(**item.dict(), orders=[])
        async with db_session() as session:
            session.add(entity)
            try:
                await session.commit()
            except IntegrityError:
                logger.warning(f"Duplicate record found for Item `{item.id}`")

    @classmethod
    async def get(cls, id_: UUID) -> Optional[ItemModel]:
        query = select(Item).where(Item.id == id_)
        async with db_session() as session:
            res = await session.execute(query)
            entity: Optional[Item] = res.scalar_one_or_none()

            if entity is None:
                return None

            return ItemModel.from_entity(entity)

    @classmethod
    async def get_categories(cls) -> list[str]:
        query = select(Item.category).distinct()
        async with db_session() as session:
            res = await session.execute(query)
            categories: list[str] = res.scalars().all()

            return categories

    @classmethod
    async def get_items_in_category(cls, category: str) -> list[ItemModel]:
        query = select(Item).where(Item.category == category)

        async with db_session() as session:
            res = await session.execute(query)
            entities: list[Item] = res.scalars().all()

            return list(map(ItemModel.from_entity, entities))

    @classmethod
    async def update_item(cls, item_info: UpdateItem):
        query = update(Item).where(Item.id == item_info.id).values(item_info.dict())

        async with db_session() as session:
            res = await session.execute(query)
            if res.rowcount == 0:
                raise NotFoundException("Item not found")
            await session.commit()
