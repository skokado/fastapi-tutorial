import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class AddProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request,
                       call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = round(time.time() - start_time, 5)
        response.headers["X-Process-Time"] = str(process_time)
        return response
