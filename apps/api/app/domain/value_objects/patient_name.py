"""
Patient name value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PatientName:
    """Represents a patient's full name."""

    first_name: str
    last_name: str

    def __post_init__(self) -> None:
        first = self.first_name.strip()
        last = self.last_name.strip()

        if not first:
            raise ValueError("First name cannot be empty.")

        if not last:
            raise ValueError("Last name cannot be empty.")

        object.__setattr__(self, "first_name", first)
        object.__setattr__(self, "last_name", last)

    @property
    def full_name(self) -> str:
        """Returns the patient's full name."""
        return f"{self.first_name} {self.last_name}"