import logging

from fastapi import FastAPI

from services.logger.config import log_config
from services.scheduler.tasks import scheduler
from services.mongo.connection import MongoDB

from apps import models

from core.config import mongo_settings

from logging.config import dictConfig


async def init_logger():
    dictConfig(log_config.model_dump())
    return logging.getLogger(log_config.LOGGER_NAME)


async def init_scheduler():
    scheduler.start()


async def init_mongo():
    await MongoDB(
        mongo_settings.database,
        mongo_settings.user,
        mongo_settings.password,
        mongo_settings.host,
        mongo_settings.port,
    ).connect(models)


async def startup_event_handler(app: FastAPI) -> None:
    app.logger = await init_logger()
    app.logger.info("Logger initialized.")

    await init_scheduler()
    app.logger.info("Scheduled tasks started.")

    await init_mongo()
    app.logger.info("MongoDB connected.")


async def shutdown_event_handler(app: FastAPI) -> None:
    app.logger.info("App closed.")
