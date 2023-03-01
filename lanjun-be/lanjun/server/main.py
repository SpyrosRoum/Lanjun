import logging

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request

from lanjun.common.settings import LOGGING_LEVEL
from lanjun.exceptions import AppException, AuthorizationException, NotFoundException, UserExists
from lanjun.server.routes import auth, health, items

logging.getLogger().setLevel(LOGGING_LEVEL)


logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(items.router)
app.include_router(auth.router)


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
