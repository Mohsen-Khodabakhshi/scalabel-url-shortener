import logging

from services.logger.config import log_config

from logging.config import dictConfig


async def init_logger():
    dictConfig(log_config.model_dump())
    return logging.getLogger(log_config.LOGGER_NAME)
