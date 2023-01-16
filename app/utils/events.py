from app.schemas.events import EventBase
from app.models.events import events_table
from app.models.database import database


async def create_event(event: EventBase, status, date_time, timeout):
    query = events_table.insert().values(name=event.name, description=event.description, date_time=date_time,
                                         timeout=timeout, status=status)
    await database.execute(query)


async def get_event(event_id: int):
    query = events_table.select().where(events_table.c.id == event_id)
    return await database.fetch_one(query)


async def get_event_date():
    query = events_table.select()