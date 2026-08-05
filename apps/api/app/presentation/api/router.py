from fastapi import APIRouter

from app.presentation.api.routes.follow_up import (
    router as follow_up_router,
)
from app.presentation.api.routes.health import (
    router as health_router,
)

router = APIRouter()

router.include_router(follow_up_router)

router.include_router(health_router)