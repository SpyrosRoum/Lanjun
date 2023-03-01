from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from lanjun.entities.links import OrderItemLink

if TYPE_CHECKING:
    from lanjun.entities.order import Order


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    name: str = Field(nullable=False, unique=True)
    description: str
    price: Decimal
    category: str
    image_url: str

    orders: list["Order"] = Relationship(back_populates="items", link_model=OrderItemLink)
