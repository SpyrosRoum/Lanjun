import logging

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from starlette.requests import Request

from lanjun.common.settings import LOGGING_LEVEL
from lanjun.exceptions import AppException, AuthorizationException, NotFoundException
from lanjun.server.routes import health

logging.getLogger().setLevel(LOGGING_LEVEL)


logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(health.router)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    if isinstance(exc, NotFoundException):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, AuthorizationException):
        status_code = status.HTTP_401_UNAUTHORIZED
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse({"detail": str(exc)}, status_code=status_code)
