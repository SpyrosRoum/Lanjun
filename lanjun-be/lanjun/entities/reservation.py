from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from lanjun.entities.links import ReservationTableLink

if TYPE_CHECKING:
    from lanjun.entities.order import Order
    from lanjun.entities.table import Table
    from lanjun.entities.user import User


class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    user_id: UUID = Field(nullable=False, foreign_key="users.id", index=True)
    starting_at: datetime
    completed_at: Optional[datetime]
    order_id: Optional[UUID] = Field(nullable=True, foreign_key="orders.id")

    user: "User" = Relationship(back_populates="reservations")
    order: "Order" = Relationship(back_populates="reservation")
    tables: list["Table"] = Relationship(
        back_populates="reservations", link_model=ReservationTableLink
    )
