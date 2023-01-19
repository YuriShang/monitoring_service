from sqlalchemy import Table, Column, String, Integer, DateTime
from sqlalchemy import MetaData

# Метаданные
metadata = MetaData()

# Модель событий
events_table = Table('events', metadata,
                     Column('id', Integer, unique=True, primary_key=True, autoincrement=True),
                     Column('service_name', String(length=255), nullable=False),
                     Column('event_name', String(length=255), nullable=False),
                     Column('description', String, nullable=False),
                     Column('event_time', DateTime, nullable=False),
                     Column('timeout', Integer, nullable=False),
                     Column('status', String, nullable=False)
                     )
