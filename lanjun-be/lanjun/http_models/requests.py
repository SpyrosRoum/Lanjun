from decimal import Decimal
from typing import Optional

from email_validator import validate_email
from pydantic import BaseModel, EmailStr, validator


class CreateUser(BaseModel):
    email: EmailStr
    name: str
    password: str

    address: Optional[str]
    floor: Optional[str]
    bell: Optional[str]

    phone: str

    @validator("email")
    def valid_email(cls, email: str) -> str:  # noqa
        return validate_email(email).email.lower()  # type: ignore


class AuthUser(BaseModel):
    email: EmailStr
    password: str

    @validator("email")
    def valid_email(cls, email: str) -> str:  # noqa
        return validate_email(email).email.lower()  # type: ignore


class CreateItem(BaseModel):
    name: str
    image_url: str
    description: str
    category: str
    price: Decimal
