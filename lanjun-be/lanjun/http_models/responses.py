from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from lanjun.domain.enums import UserType
from lanjun.domain.item import ItemModel
from lanjun.domain.user import UserModel


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


class UserResponse(BaseModel):
    email: str
    name: str
    address: Optional[str]
    floor: Optional[str]
    bell: Optional[str]
    phone: str
    type: UserType

    @classmethod
    def from_model(cls, user: UserModel) -> "UserResponse":
        return cls(**user.dict())
