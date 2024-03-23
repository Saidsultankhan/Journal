import pytest


@pytest.mark.django_db
@pytest.fixture
def subject_teacher_create(subject_teacher_factory):
    subject_teacher = subject_teacher_factory.create()

    return subject_teacher


@pytest.mark.django_db
@pytest.fixture
def subject_teacher_list(subject_teacher_factory):
    subject_teachers = subject_teacher_factory.create_batch(3)

    return subject_teachers
