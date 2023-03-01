from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from lanjun.entities.item import Item


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
