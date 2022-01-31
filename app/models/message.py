from pydantic import BaseModel


class MessageIn(BaseModel):
    channel: str
    message: dict
