from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from lanjun.domain.enums import UserType
from lanjun.entities.user import User


class UserModel(BaseModel):
    id: UUID
    email: str
    name: str
    address: Optional[str]
    floor: Optional[str]
    bell: Optional[str]
    phone: str
    password: str
    type: UserType

    @classmethod
    def from_entity(cls, entity: User) -> "UserModel":
        return cls(**entity.dict())
