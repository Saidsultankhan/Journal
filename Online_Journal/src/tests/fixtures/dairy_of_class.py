import pytest


@pytest.mark.django_db
@pytest.fixture
def teacher_create_for_dairy(teacher_factory, user_for_teacher_create):
    teacher = teacher_factory.create(user=user_for_teacher_create)

    return teacher
