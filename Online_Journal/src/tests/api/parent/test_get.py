import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_parent_get(parent_create):
    response = api_client.get(f'/api/v1/parent_detail/{parent_create.id}/')

    assert response.data['user'] == parent_create.user.id
