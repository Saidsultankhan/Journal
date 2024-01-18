import pytest


@pytest.mark.django_db
@pytest.fixture
def parent_create(parent_factory):
    parent = parent_factory.create()

    return parent


@pytest.mark.django_db
@pytest.fixture
def parents_list(parent_factory):
    parent = parent_factory.create_batch(3)

    return parent
