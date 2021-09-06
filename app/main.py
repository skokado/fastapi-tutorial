import os

from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.core.config import settings
from app.routers import blogs, users, auth
from app.middlewares import AddProcessTimeHeaderMiddleware

DEBUG = bool(os.getenv('DEBUG', False))
if DEBUG:
    app = FastAPI(title=settings.SERVER_NAME)
else:
    app = FastAPI(
        title=settings.SERVER_NAME,
        docs_url=None,
        redoc_url=None,
    )

# Register routers
api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(blogs.router)

app.include_router(api_router, prefix=settings.API_V1_STR)

# Register MiddleWares
app.add_middleware(AddProcessTimeHeaderMiddleware)
