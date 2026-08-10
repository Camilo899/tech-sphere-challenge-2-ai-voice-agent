from dotenv import load_dotenv
from fastapi import FastAPI

from app.presentation.api.exception_handlers import (
    register_exception_handlers,
)
from app.presentation.api.router import router

load_dotenv()

app = FastAPI(
    title="Clinical AI Voice Agent",
    version="0.1.0",
)

register_exception_handlers(app)

app.include_router(router)