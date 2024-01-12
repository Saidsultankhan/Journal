import pytest
from pytest_factoryboy import register
from .factories import (
    UserFactory,
    ParentFactory,
    TeacherFactory,
    GradeFactory,
    PupilFactory,
)

register(UserFactory)
register(ParentFactory)
register(TeacherFactory)
register(GradeFactory)
register(PupilFactory)


@pytest.mark.django_db
@pytest.fixture
def user_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.save()

    return user


@pytest.mark.django_db
@pytest.fixture
def admin_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.is_staff = True
    user.save()
    return user


@pytest.mark.django_db
@pytest.fixture
def parent_create(parent_factory):
    parent = parent_factory.create()

    return parent


@pytest.mark.django_db
@pytest.fixture
def teacher_create(teacher_factory):
    teacher = teacher_factory.create()

    return teacher



# @pytest.mark.django_db
# @pytest.fixture
# def pupil_create(pupil_factory):
#     pupil = pupil_factory.create()
#     return pupil

