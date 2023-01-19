from app.schemas.events import EventBase
from app.models.events import events_table
from app.models.database import database


# Создаем событие
async def create_event(event: EventBase, status, event_time, timeout):
    query = events_table.insert().values(service_name=event.service_name, event_name=event.event_name,
                                         description=event.description, event_time=event_time,
                                         timeout=timeout, status=status)
    await database.execute(query)


# Получаем событие по его id
async def get_event(event_id: int):
    query = events_table.select().where(events_table.c.id == event_id)
    return await database.fetch_one(query)


# Получаем список с указанным количеством последних событий
async def get_event_list(service_name, chunk_size):
    query = events_table.select().where(events_table.c.service_name == service_name) \
        .order_by(events_table.c.id.desc()).limit(chunk_size)
    return await database.fetch_all(query)


# Получаем время последнего события для вычисления таймаута
async def get_event_time(service_name):
    query = events_table.select().where(events_table.c.service_name == service_name) \
        .order_by(events_table.c.event_time.desc())
    return await database.fetch_one(query)
