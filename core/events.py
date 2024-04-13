from fastapi import FastAPI

from services.events import init_logger


async def startup_event_handler(app: FastAPI) -> None:
    app.logger = await init_logger()
    app.logger.info("Logger initialized.")


async def shutdown_event_handler(app: FastAPI) -> None:
    app.logger.info("App closed.")
