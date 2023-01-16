import asyncio
from aiohttp import web
from app.utils.config import config
from app.models.database import database
from app.routes.routes import EventView


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
    app.router.add_view("/test", EventView)

    return app


if __name__ == "__main__":
    app = init_app()
    web.run_app(app, port=config["common"]["port"])