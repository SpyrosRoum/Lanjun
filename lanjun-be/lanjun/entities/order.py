from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from lanjun.entities.links import OrderItemLink

if TYPE_CHECKING:
    from lanjun.entities.item import Item
    from lanjun.entities.reservation import Reservation
    from lanjun.entities.user import User


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    user_id: UUID = Field(nullable=False, foreign_key="users.id", index=True)
    cost: Decimal
    prepaid: bool
    created_at: datetime

    user: "User" = Relationship(back_populates="orders")
    reservation: "Reservation" = Relationship(back_populates="order")
    items: list["Item"] = Relationship(back_populates="orders", link_model=OrderItemLink)
