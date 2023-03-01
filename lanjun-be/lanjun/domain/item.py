from decimal import Decimal
from uuid import UUID, uuid4

from pydantic import BaseModel

from lanjun.entities.item import Item
from lanjun.http_models.requests import CreateItem


class ItemModel(BaseModel):
    id: UUID
    name: str
    description: str
    price: Decimal
    category: str
    image_url: str

    @classmethod
    def from_entity(cls, entity: Item) -> "ItemModel":
        return cls(**entity.dict())

    @classmethod
    def from_item_create_info(cls, info: CreateItem) -> "ItemModel":
        return cls(id=uuid4(), **info.dict())
