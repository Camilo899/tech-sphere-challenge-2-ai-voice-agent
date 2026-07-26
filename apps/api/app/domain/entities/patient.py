from dataclasses import dataclass
from uuid import UUID


@dataclass
class Patient:
    """
    Represents a patient enrolled in a postoperative follow-up.
    """

    id: UUID
    first_name: str
    last_name: str