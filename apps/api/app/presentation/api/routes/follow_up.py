from fastapi import APIRouter, Depends

from app.application.dtos.start_follow_up_request import (
    StartFollowUpRequest,
)
from app.application.dtos.start_follow_up_response import (
    StartFollowUpResponse,
)
from app.application.use_cases.start_follow_up import (
    StartFollowUpUseCase,
)
from app.presentation.api.dependencies import (
    get_start_follow_up_use_case,
)
from app.presentation.schemas.start_follow_up_request_schema import (
    StartFollowUpRequestSchema,
)
from app.presentation.schemas.start_follow_up_response_schema import (
    StartFollowUpResponseSchema,
)

router = APIRouter(
    prefix="/follow-up",
    tags=["Follow Up"],
)


@router.post(
    "/start",
    response_model=StartFollowUpResponseSchema,
)
def start_follow_up(
    request: StartFollowUpRequestSchema,
    use_case: StartFollowUpUseCase = Depends(
        get_start_follow_up_use_case,
    ),
) -> StartFollowUpResponseSchema:
    dto = StartFollowUpRequest(
        patient_id=request.patient_id,
    )

    result: StartFollowUpResponse = use_case.execute(dto)

    return StartFollowUpResponseSchema(
        conversation_id=result.conversation_id,
        current_state=result.current_state,
    )