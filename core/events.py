import logging

from fastapi import FastAPI

from services.events import init_logger, init_scheduler


async def startup_event_handler(app: FastAPI) -> None:
    app.logger = await init_logger()
    app.logger.info("Logger initialized.")

    await init_scheduler()
    app.logger.info("Scheduled tasks started.")


async def shutdown_event_handler(app: FastAPI) -> None:
    app.logger.info("App closed.")
