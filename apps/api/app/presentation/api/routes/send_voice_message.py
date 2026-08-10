from fastapi import APIRouter, Depends, File, UploadFile

from app.application.use_cases.send_voice_message import (
    SendVoiceMessageUseCase,
)
from app.presentation.api.dependencies import (
    get_send_voice_message_use_case,
)
from app.presentation.schemas.send_voice_message_response_schema import (
    SendVoiceMessageResponseSchema,
)

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)


@router.post(
    "/voice",
    response_model=SendVoiceMessageResponseSchema,
)
async def send_voice_message(
    conversation_id: str,
    audio: UploadFile = File(...),
    use_case: SendVoiceMessageUseCase = Depends(
        get_send_voice_message_use_case,
    ),
) -> SendVoiceMessageResponseSchema:
    audio_bytes = await audio.read()

    result = use_case.execute(
        conversation_id=conversation_id,
        audio=audio_bytes,
        mime_type=audio.content_type or "application/octet-stream",
    )

    return SendVoiceMessageResponseSchema(
        response=result.response,
        current_state=result.current_state,
    )