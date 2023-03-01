from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from lanjun.domain.item import ItemModel


class ItemResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: Decimal
    image: str

    @classmethod
    def from_model(cls, model: ItemModel) -> "ItemResponse":
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            price=model.price,
            image=model.image_url,
        )


class Category(BaseModel):
    name: str
    items: list[ItemResponse]


class CategoryItems(BaseModel):
    categories: list[Category]


class UserCreated(BaseModel):
    id: UUID


class LoginToken(BaseModel):
    token: str
