from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import Column
from sqlmodel import Field, Relationship, SQLModel

from lanjun.common.sqlmodel_fields import EnumField
from lanjun.domain.enums import UserType

if TYPE_CHECKING:
    from lanjun.entities.order import Order


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    email: str = Field(nullable=False, unique=True, index=True)
    name: str
    address: Optional[str]
    floor: Optional[str]
    bell: Optional[str]
    phone: str = Field(nullable=False, unique=True)
    password: str
    type: UserType = Field(sa_column=Column(EnumField(UserType)))

    orders: list["Order"] = Relationship(back_populates="user")
