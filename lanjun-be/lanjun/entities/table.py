from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlmodel import Field, SQLModel, Relationship

from lanjun.entities.reservation import ReservationTableLink

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
