import os
from collections.abc import AsyncGenerator

import pytest
from alembic import command
from alembic.config import Config
from sqlmodel import SQLModel

from lanjun import entities  # noqa: F401
from lanjun.common import settings
from lanjun.database import get_or_create_engine


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
