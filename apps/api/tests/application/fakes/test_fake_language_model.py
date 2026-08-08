from app.application.fakes.fake_language_model import (
    FakeLanguageModel,
)


def test_fake_language_model_returns_response() -> None:
    model = FakeLanguageModel()

    response = model.generate(
        prompt="Paciente con fiebre postoperatoria.",
    )

    assert response.content == "Respuesta clínica simulada."
    assert response.evidence_used == ("chunk-001",)


def test_fake_language_model_keeps_last_prompt() -> None:
    model = FakeLanguageModel()

    prompt = "Paciente con dolor postoperatorio."

    model.generate(prompt=prompt)

    assert model.last_prompt == prompt