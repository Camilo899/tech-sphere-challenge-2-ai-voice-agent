from fastapi import FastAPI

from app.presentation.api.router import (
    router,
)

app = FastAPI(
    title="Clinical AI Voice Agent",
    version="0.1.0",
)

app.include_router(router)