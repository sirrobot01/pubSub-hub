import json
from fastapi import APIRouter, Request
from app.models import message as models
from app.services import broadcast

router = APIRouter(
    tags=["messages"]
)


@router.post("/")
async def send_message(payload: models.MessageIn):
    await broadcast.publish(payload.channel, json.dumps(payload.message))
    