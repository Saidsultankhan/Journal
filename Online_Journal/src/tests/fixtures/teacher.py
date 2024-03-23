import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def teachers_list(teacher_factory):
    teachers = teacher_factory.create_batch(3)

    return teachers
