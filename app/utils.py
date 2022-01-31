from functools import lru_cache
from typing import List, Optional

from fastapi import FastAPI, WebSocket

import aioredis

@lru_cache
def get_redis(app: FastAPI):
    redis: aioredis.Redis = app.extra.get("redis")
    return redis
