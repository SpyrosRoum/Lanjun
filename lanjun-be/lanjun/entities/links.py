from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ReservationTableLink(SQLModel, table=True):
    __tablename__ = "reservation_tables"
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    res_id: UUID = Field(foreign_key="reservations.id")
    table_id: UUID = Field(foreign_key="tables.id")


class OrderItemLink(SQLModel, table=True):
    __tablename__ = "order_items"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    order_id: UUID = Field(foreign_key="orders.id")
    item_id: UUID = Field(foreign_key="items.id")
    item_count: int
