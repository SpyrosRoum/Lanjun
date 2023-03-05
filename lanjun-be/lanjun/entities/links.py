from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class OrderItemLink(SQLModel, table=True):
    __tablename__ = "order_items"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    order_id: UUID = Field(foreign_key="orders.id")
    item_id: UUID = Field(foreign_key="items.id")
    item_count: int
