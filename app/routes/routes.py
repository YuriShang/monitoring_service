from aiohttp import web
from aiohttp_pydantic import PydanticView
from datetime import datetime
from app.schemas import events
from app.utils.events import create_event, get_event, get_event_time, get_event_list
from app.utils.services import timeout_control


class EventView(PydanticView):
    # Создаем событие
    async def post(self, event: events.EventBase):
        last_event_time = await get_event_time(event.service_name)
        if last_event_time is not None:
            event_status, timeout = await timeout_control(last_event_time.event_time)
        else:
            event_status, timeout = 'FIRST EVENT', 0
        current_time = datetime.now()
        await create_event(event=event, status=event_status, timeout=timeout, event_time=current_time)
        result = event.dict()
        result.update({"status": event_status, "timeout": timeout,
                       "event_time": current_time.strftime("%Y-%m-%d %H:%M:%S")})
        return web.json_response(result)

    # Получаем событие по его id
    async def get(self, event_id: int):
        event = await get_event(event_id)
        if event is not None:
            current_event = {event.id: {"service_name": event.service_name, "event_name": event.event_name,
                                        "description": event.description,
                                        "event_time": event.event_time.strftime("%Y-%m-%d %H:%M:%S"),
                                        "timeout": event.timeout, "status": event.status}}
            return web.json_response(current_event)
        return web.json_response({"result": f"event with id={event_id} does not exist"})


# Получаем список с указанным количеством последних событий
class EventList(PydanticView):
    async def get(self, service: str, chunk_size: int):
        """
        :param str service: Название сервиса
        :param int chunk_size: Количество событий в списке
        """
        event_list = await get_event_list(service, chunk_size)
        event_list.reverse()
        if event_list is not None:
            all_events = {}
            for event in event_list:
                current_event = {event.id: {"service_name": event.service_name, "event_name": event.event_name,
                                            "description": event.description,
                                            "event_time": event.event_time.strftime("%Y-%m-%d %H:%M:%S"),
                                            "timeout": event.timeout, "status": event.status}}
                all_events.update(current_event)
            return web.json_response(all_events)
        return web.json_response({"result": "empty list"})
