import logging
import re
import time
import typing
from collections.abc import Awaitable, Callable
from typing import Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLogMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: FastAPI,
        *,
        logger: typing.Optional[logging.Logger] = None,
        skip_routes: Optional[list[str]] = None,
        skip_regexes: Optional[list[str]] = None,
    ):
        self._logger = logger if logger else logging.getLogger(__name__)
        self._skip_routes = skip_routes if skip_routes else ["/health"]
        self._skip_regexes = (
            list(map(lambda regex: re.compile(regex), skip_regexes)) if skip_regexes else []
        )
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if self._should_route_be_skipped(request):
            return await call_next(request)

        return await self._execute_request_with_logging(request, call_next)

    def _should_route_be_skipped(self, request: Request) -> bool:
        return any(
            [True for path in self._skip_routes if request.url.path.startswith(path)]
            + [True for regex in self._skip_regexes if regex.match(request.url.path)]
        )

    async def _execute_request_with_logging(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request_ident = uuid4()

        start_time = time.perf_counter()
        self._log_request_received(request, request_ident)

        response = await self._execute_request(call_next, request, request_ident)

        finish_time = time.perf_counter()
        self._log_request_completed(request, response, finish_time - start_time, request_ident)

        return response

    def _log_request_received(self, request: Request, request_ident: UUID) -> None:
        self._logger.info(
            f"Request {request.method} {request.url.path} received [{request_ident}]",
        )
        self._logger.debug(f"Request [{request_ident}] Headers: {request.headers}")

    def _log_request_completed(
        self, request: Request, response: Response, execution_time: float, request_ident: UUID
    ) -> None:
        result = "completed" if response.status_code < 400 else "failed"

        self._logger.info(
            f"Request [{request_ident}] {request.method} {request.url.path} {result}, status_code={response.status_code}",
        )

    async def _execute_request(
        self,
        call_next: Callable[[Request], Awaitable[Response]],
        request: Request,
        request_ident: UUID,
    ) -> Response:
        try:
            response = await call_next(request)
        except Exception:
            self._logger.exception(
                f"Request [{request_ident}] failed with exception {request.url.path}, method={request.method}",
            )
            raise
        return response
