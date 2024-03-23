import pytest


@pytest.mark.django_db
@pytest.fixture
def subject_create(subject_factory):
    subject = subject_factory.create()

    return subject


@pytest.mark.django_db
@pytest.fixture
def subjects_list(subject_factory):
    subjects = subject_factory.create_batch(3)

    return subjects
