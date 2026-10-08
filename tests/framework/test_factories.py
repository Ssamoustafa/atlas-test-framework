from atlas.factories import user_factory


def test_user_factory_produces_unique_emails() -> None:
    assert user_factory().email != user_factory().email
