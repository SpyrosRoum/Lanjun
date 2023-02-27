from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from lanjun.domain.item import ItemModel


class ItemResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: Decimal
    count: int
    image: str

    @classmethod
    def from_model(cls, model: ItemModel) -> "ItemResponse":
        return cls(image=model.image_url, **model.dict())


class Category(BaseModel):
    name: str
    items: list[ItemResponse]


class CategoryItems(BaseModel):
    categories: list[Category]


class UserCreated(BaseModel):
    id: UUID
