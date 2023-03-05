import logging
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from lanjun.database import db_session
from lanjun.domain.enums import UserType
from lanjun.domain.user import UserModel
from lanjun.entities.user import User
from lanjun.exceptions import UserExists
from lanjun.http_models.requests import CreateUser

logger = logging.getLogger(__name__)


class UserRepo:
    @classmethod
    async def save(cls, user: UserModel) -> None:
        entity = User(**user.dict())
        async with db_session() as session:
            session.add(entity)
            try:
                await session.commit()
            except IntegrityError:
                logger.warning(f"Duplicate record found for User `{user.id}`")

    @classmethod
    async def get(cls, id_: UUID) -> Optional[UserModel]:
        query = select(User).where(User.id == id_)

        async with db_session() as session:
            res = await session.execute(query)
            entity: Optional[User] = res.scalar_one_or_none()

            if entity is None:
                return None

            return UserModel.from_entity(entity)

    @classmethod
    async def create_new_user(
        cls, user: CreateUser, hashed_pwd: bytes, user_type: UserType
    ) -> UUID:
        user_dict = user.dict()
        user_dict.pop("password")
        entity = User(
            **user_dict,
            password=hashed_pwd,
            type=user_type,
            orders=[],
            reservations=[],
        )
        user_id = entity.id

        async with db_session() as session:
            session.add(entity)
            try:
                await session.commit()
            except IntegrityError as exc:
                raise UserExists() from exc
            else:
                return user_id

    @classmethod
    async def get_from_email(cls, email: str) -> Optional[UserModel]:
        query = select(User).where(User.email == email)

        async with db_session() as session:
            res = await session.execute(query)
            entity: Optional[User] = res.scalar_one_or_none()

            if entity is None:
                return None

            return UserModel.from_entity(entity)
