from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from lanjun.entities.links import ReservationTableLink

if TYPE_CHECKING:
    from lanjun.entities.reservation import Reservation


class Table(SQLModel, table=True):
    __tablename__ = "tables"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    location: str
    capacity: int = Field(nullable=False, gt=0)

    reservations: list["Reservation"] = Relationship(
        back_populates="tables", link_model=ReservationTableLink
    )
