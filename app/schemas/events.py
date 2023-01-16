from pydantic import BaseModel
from typing import Optional


class EventBase(BaseModel):
    name: str
    description: str