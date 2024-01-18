import pytest


@pytest.mark.django_db
@pytest.fixture
def pupil_create(pupil_factory):
    pupil = pupil_factory.create()

    return pupil


@pytest.mark.django_db
@pytest.fixture
def pupils_list(pupil_factory):
    pupils = pupil_factory.create_batch(3)

    return pupils
