import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def grade_create(grade_factory):
    grade = grade_factory.create()

    return grade


@pytest.mark.django_db
@pytest.fixture
def grades_list(grade_factory):
    grades = grade_factory.create_batch(3)
    return grades
