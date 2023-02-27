import os
from asyncio import AbstractEventLoop
from collections.abc import AsyncGenerator

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
