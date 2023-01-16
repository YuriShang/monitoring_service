import databases
from app.utils.config import config

database = databases.Database(config["postgres"]["database_url"])