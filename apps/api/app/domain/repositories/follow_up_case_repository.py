from typing import Protocol

from app.domain.entities.follow_up_case import FollowUpCase


class FollowUpCaseRepository(Protocol):
    """
    Repository abstraction for FollowUpCase persistence.
    """

    async def save(self, case: FollowUpCase) -> None:
        ...

    async def get(self, case_id):
        ...