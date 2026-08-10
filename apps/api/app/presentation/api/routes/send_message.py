from fastapi import APIRouter, Depends

from app.application.dtos.send_message_request import (
    SendMessageRequest,
)
from app.application.dtos.send_message_response import (
    SendMessageResponse,
)
from app.application.use_cases.send_message import (
    SendMessageUseCase,
)
from app.presentation.api.dependencies import (
    get_send_message_use_case,
)
from app.presentation.schemas.send_message_request_schema import (
    SendMessageRequestSchema,
)
from app.presentation.schemas.send_message_response_schema import (
    SendMessageResponseSchema,
)

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)


@router.post(
    "",
    response_model=SendMessageResponseSchema,
)
def send_message(
    request: SendMessageRequestSchema,
    use_case: SendMessageUseCase = Depends(
        get_send_message_use_case,
    ),
) -> SendMessageResponseSchema:
    dto = SendMessageRequest(
        conversation_id=request.conversation_id,
        message=request.message,
    )

    result: SendMessageResponse = use_case.execute(dto)

    return SendMessageResponseSchema(
        response=result.response,
        current_state=result.current_state,
        clinical_decision=result.clinical_decision,
    )