from fastapi import APIRouter

router = APIRouter(
    prefix="/follow-up",
    tags=["Follow Up"],
)


@router.post("/start")
def start_follow_up() -> dict[str, str]:
    """
    Starts a postoperative follow-up conversation.
    """
    return {
        "status": "ok",
    }