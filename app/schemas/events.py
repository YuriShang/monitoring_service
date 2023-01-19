from pydantic import BaseModel


class EventBase(BaseModel):
    service_name: str
    event_name: str
    description: str
