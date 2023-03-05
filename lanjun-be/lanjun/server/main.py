import logging

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request

from lanjun.common.logging import setup_logger
from lanjun.exceptions import AppException, AuthorizationException, NotFoundException, UserExists
from lanjun.server.middlewares.log import RequestLogMiddleware
from lanjun.server.routes import auth, health, items, orders, users

setup_logger()

logger = logging.getLogger(__name__)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLogMiddleware)

app.include_router(health.router)
app.include_router(items.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    if isinstance(exc, NotFoundException):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, AuthorizationException):
        status_code = status.HTTP_401_UNAUTHORIZED
    elif isinstance(exc, UserExists):
        status_code = status.HTTP_400_BAD_REQUEST
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse({"detail": str(exc)}, status_code=status_code)
