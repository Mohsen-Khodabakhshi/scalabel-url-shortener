from fastapi import FastAPI

from core import events

from helper.responses import Response, Message

app = FastAPI(default_response_class=Response)


@app.on_event("startup")
async def startup_event() -> None:
    await events.startup_event_handler(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await events.shutdown_event_handler(app)


@app.get("/health", response_model=Message)
async def health():
    return Message(message="It's ok.")
