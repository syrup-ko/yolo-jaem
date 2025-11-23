from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.config import settings
from app.api.routes.simulation_router import router as simulation_router
from app.api.routes.asset_router import router as asset_router
from app.api.routes.user_router import router as user_router
from app.core.cache import init_redis, close_redis

limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])

app = FastAPI(title=settings.PROJECT_NAME)

app.add_exception_handler(RateLimitExceeded, lambda r, e: e)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulation_router, prefix=settings.API_V1_STR)
app.include_router(asset_router, prefix=settings.API_V1_STR)
app.include_router(user_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def on_startup():
    await init_redis()


@app.on_event("shutdown")
async def on_shutdown():
    await close_redis()



