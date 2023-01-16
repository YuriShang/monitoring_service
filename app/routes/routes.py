from aiohttp import web
from aiohttp_pydantic import PydanticView
from datetime import datetime
from app.schemas import events
from app.utils.events import create_event, get_event
from app.utils.services import timeout_control


class EventView(PydanticView):
    async def post(self, event: events.EventBase):
        event_status, timeout = await timeout_control(event.name)
        res = await create_event(event=event, status=event_status, timeout=timeout, date_time=datetime.now())
        return web.json_response()

    async def get(self, event_id: int):
        res = await get_event(event_id)
        return res
