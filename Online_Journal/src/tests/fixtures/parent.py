import pytest


@pytest.mark.django_db
@pytest.fixture
def parents_list(parent_factory):
    parent = parent_factory.create_batch(3)

    return parent


@pytest.mark.django_db
@pytest.fixture
def parent_create_to_login(parent_factory, user_for_parent_create):
    teacher = parent_factory.create(user=user_for_parent_create)

    return teacher
