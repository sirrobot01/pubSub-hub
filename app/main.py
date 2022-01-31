from fastapi import FastAPI, WebSocket
from app.services import broadcast
from app.api import channel as channel_router, message as message_router

app = FastAPI(
    on_startup=[broadcast.connect],
    on_shutdown=[broadcast.disconnect]
)

REDIS_URL = 'redis://localhost:6379'

app.include_router(channel_router.router, prefix="/channels")
app.include_router(message_router.router, prefix="/messages")

@app.get("/")
async def get():
    return {'status': True}

@app.websocket("/channels/{channel_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: str):
    await websocket.accept()
    async with broadcast.subscribe(channel_id) as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)
