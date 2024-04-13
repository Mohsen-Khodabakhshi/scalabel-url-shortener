from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class MongoSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str | None = None
    password: str | None = None
    database: str = "app"

    class Config:
        env_prefix = "MONGO_"


mongo_settings = MongoSettings()
