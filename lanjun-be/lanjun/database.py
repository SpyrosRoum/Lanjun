import json
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Dict

import pydantic.json
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from lanjun.common.settings import DATABASE_URL

_db_engines: Dict[str, AsyncEngine] = {}


def _pydantic_json_serializer(*args: Any, **kwargs: Any) -> str:
    """
    Encodes json in the same way that pydantic does.
    """
    return json.dumps(*args, default=pydantic.json.pydantic_encoder, **kwargs)


def get_or_create_engine(url: str = DATABASE_URL, echo: bool = False) -> AsyncEngine:
    key = url + str(echo)

    if key not in _db_engines:
        options = {
            "echo": echo,
            "future": True,
            "json_serializer": _pydantic_json_serializer,
        }

        engine = create_async_engine(url, **options)
        _db_engines[key] = engine

    return _db_engines[key]


def get_session(url: str = DATABASE_URL, echo: bool = False) -> AsyncSession:
    engine = get_or_create_engine(url, echo)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)

    return async_session()


@asynccontextmanager
async def db_session(
    url: str = DATABASE_URL, echo: bool = False
) -> AsyncGenerator[AsyncSession, None]:
    session = get_session(url, echo)
    try:
        yield session
    finally:
        await session.close()
