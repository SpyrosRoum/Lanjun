import os

import pytest
from alembic import command
from alembic.config import Config

from lanjun.common import settings


@pytest.fixture(scope="package", autouse=True)
def migrate_db() -> None:
    settings.DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5441/lanjun"
    root = os.path.join(os.path.dirname(__file__))
    alembic_config = os.path.join(root, "../../alembic.ini")
    config = Config(alembic_config)
    command.upgrade(config, "head")
