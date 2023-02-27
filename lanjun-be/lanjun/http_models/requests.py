from typing import Optional

from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    name: str
    password: str

    address: Optional[str]
    floor: Optional[str]
    bell: Optional[str]

    phone: str
