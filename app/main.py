import logging
from aiohttp import web
from app.models.database import database
from app.routes.routes import EventView, EventList


# Подключаемся к БД при старте приложения
async def startup(app):
    return await database.connect()


# Отключаемся при останове
async def cleanup(app):
    return await database.disconnect()


# Инициализируем приложение
def init_app():
    app = web.Application()
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    # Настраивем пути
    app.router.add_view("/event", EventView)
    app.router.add_view("/event_list", EventList)
    return app


if __name__ == "__main__":
    app = init_app()
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=8000)
