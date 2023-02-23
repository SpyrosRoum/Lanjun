from typing import Any

from sqlmodel import Enum as SQLModelEnum


class EnumField(SQLModelEnum):
    def __init__(self, *enums: Any, **kw: Any) -> None:
        """
        SQLModel Enum by default stores the keys in the database, not values.
        for example:
        class MyEnum(enum.Enum):
            one = 1
            two = 2
            three = 3
        Using the SQLModel Enum as is, the string names of each element,
        e.g. "one", "two", "three", are persisted to the database.
        In order to persist the values they have suggested the values_callable approach.
        """
        kw["values_callable"] = lambda x: [e.value for e in x]
        super().__init__(*enums, **kw)
