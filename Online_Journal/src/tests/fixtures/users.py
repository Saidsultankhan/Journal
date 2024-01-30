import pytest


@pytest.mark.django_db
@pytest.fixture
def parent_create(parent_factory):
    parent = parent_factory.create()

    return parent


@pytest.mark.django_db
@pytest.fixture
def pupil_create(pupil_factory):
    pupil = pupil_factory.create()

    return pupil


@pytest.mark.django_db
@pytest.fixture
def teacher_create(teacher_factory, user_create):
    teacher = teacher_factory.create(user=user_create)
    return teacher
