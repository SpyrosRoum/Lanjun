from collections.abc import Callable
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

import pytest

from lanjun.domain.item import ItemModel
from lanjun.repos.item import ItemRepo


class TestItemRepo:
    async def test_save_get(self, get_item):
        ids = [uuid4(), uuid4()]
        for id_ in ids:
            item = get_item(id_=id_)
            await ItemRepo.save(item)

        for id_ in ids:
            res = await ItemRepo.get(id_)

            assert res is not None
            assert res.id in ids

    async def test_get_categories(self, get_item):
        categories = ["a", "a", "b", "c"]
        for category in categories:
            item = get_item(category=category)
            await ItemRepo.save(item)

        res = await ItemRepo.get_categories()

        assert len(res) == len(categories) - 1  # As many as unique categories
        assert len(set(res)) == len(res)  # all unique
