from app.domain.exceptions.domain_exception import DomainException


def test_should_raise_domain_exception() -> None:
    try:
        raise DomainException("Business rule violated")
    except DomainException as exc:
        assert str(exc) == "Business rule violated"