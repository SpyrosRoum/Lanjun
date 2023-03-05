import os
from asyncio import AbstractEventLoop
from collections.abc import AsyncGenerator
from decimal import Decimal
from typing import Callable, Optional
from uuid import UUID, uuid4

import pytest
from alembic import command
from alembic.config import Config
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel

from lanjun import entities  # noqa: F401
from lanjun import database
from lanjun.common import settings
from lanjun.database import get_or_create_engine
from lanjun.domain.enums import UserType
from lanjun.domain.item import ItemModel
from lanjun.domain.user import UserModel
from lanjun.server.main import app


@pytest.fixture(scope="package", autouse=True)
def migrate_db() -> None:
    settings.DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5441/lanjun"
    root = os.path.join(os.path.dirname(__file__))
    alembic_config = os.path.join(root, "../../alembic.ini")
    config = Config(alembic_config)
    command.upgrade(config, "head")


@pytest.fixture(scope="function", autouse=True)
async def truncate_all() -> AsyncGenerator[None, None]:
    try:
        yield
    finally:
        meta = SQLModel.metadata
        async with get_or_create_engine().connect() as con:
            trans = await con.begin()

            for table in reversed(meta.sorted_tables):
                await con.execute(table.delete())

            await trans.commit()


@pytest.fixture(scope="function", autouse=True)
async def test_engine(event_loop) -> AsyncEngine:
    # We need to force a new engine for every test,
    # otherwise the engine will try to use the event_loop that existed when it got created
    # but event_loops are function scoped
    database._db_engines = {}

    return get_or_create_engine()


@pytest.fixture(scope="function")
async def test_client(event_loop: AbstractEventLoop) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="function")
def get_item() -> Callable[[], ItemModel]:
    def _wrapper(
        id_: Optional[UUID] = None,
        name: Optional[str] = None,
        description: str = "item description",
        price: Decimal = Decimal("3.14"),
        category: str = "category A",
        image_url: str = "https://example.com",
    ) -> ItemModel:
        return ItemModel(
            id=id_ or uuid4(),
            name=name or str(uuid4()),  # Name must be unique
            description=description,
            price=price,
            category=category,
            image_url=image_url,
        )

    return _wrapper


@pytest.fixture(scope="function")
def get_user() -> Callable[[], UserModel]:
    def _wrapper(
        id_: Optional[UUID] = None,
        email: Optional[str] = None,
        name: str = "User Name",
        address: Optional[str] = None,
        floor: Optional[str] = None,
        bell: Optional[str] = None,
        phone: Optional[str] = None,
        password: str = "pass",
        type: UserType = UserType.NORMAL,
    ) -> UserModel:
        return UserModel(
            id=id_ or uuid4(),
            email=email or f"{str(uuid4())}@email.com",
            name=name,
            address=address,
            floor=floor,
            bell=bell,
            phone=phone or str(uuid4()),
            password=password,
            type=type,
        )

    return _wrapper
