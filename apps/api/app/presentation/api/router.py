from fastapi import APIRouter

from app.presentation.api.routes.follow_up import (
    router as follow_up_router,
)

router = APIRouter()

router.include_router(follow_up_router)