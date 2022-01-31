from fastapi import APIRouter, Request
from app.utils import get_redis

router = APIRouter(
    tags=["channels"]
)


@router.get("/")
async def get_channels(request: Request):
    redis = get_redis(request.app)
    return await redis.pubsub_channels()

