from app.domain.ports.language_model import LanguageModel


def test_language_model_is_abstract() -> None:
    try:
        LanguageModel()
    except TypeError:
        return

    raise AssertionError(
        "LanguageModel must be abstract",
    )