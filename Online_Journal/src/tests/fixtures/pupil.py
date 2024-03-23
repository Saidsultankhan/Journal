import pytest


@pytest.mark.django_db
@pytest.fixture
def pupils_list(pupil_factory):
    pupils = pupil_factory.create_batch(3)

    return pupils
