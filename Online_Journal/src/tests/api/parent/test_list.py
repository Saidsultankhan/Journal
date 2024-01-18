import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_parent_list(parents_list):
    response = api_client.get(f'/api/v1/parents/')

    assert len(response.data) == 3
    