import pytest

from app.domain.value_objects.patient_name import PatientName


def test_should_build_full_name() -> None:
    name = PatientName(
        first_name="Camilo",
        last_name="Julio",
    )

    assert name.full_name == "Camilo Julio"


def test_should_trim_spaces() -> None:
    name = PatientName(
        first_name="  Camilo ",
        last_name=" Julio  ",
    )

    assert name.first_name == "Camilo"
    assert name.last_name == "Julio"


def test_should_raise_error_for_empty_first_name() -> None:
    with pytest.raises(ValueError):
        PatientName("", "Julio")


def test_should_raise_error_for_empty_last_name() -> None:
    with pytest.raises(ValueError):
        PatientName("Camilo", "")