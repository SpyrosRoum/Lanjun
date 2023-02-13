from datetime import date
from typing import Optional

from fastapi import APIRouter, Query

router = APIRouter()


@router.get("available/tables")
@router.get("v1/available/tables")
async def get_available_tables(day: Optional[date] = Query(default=None, alias="date")):
    day = day or date.today()
