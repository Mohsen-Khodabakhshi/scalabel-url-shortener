from beanie import init_beanie

import motor.motor_asyncio


class MongoDB:
    def __init__(
        self,
        database: str,
        user: str | None = None,
        password: str | None = None,
        host: str = "localhost",
        port: int = 27017,
    ) -> None:
        if user and password:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                f"mongodb://{user}:{password}@{host}:{port}"
            )
        else:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                f"mongodb://{host}:{port}"
            )
        self.database = database

    async def connect(self, models: list) -> None:
        await init_beanie(
            database=self.client[self.database],
            document_models=models,
        )
