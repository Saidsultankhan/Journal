import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_parent_delete(parent_create):
    response = api_client.delete(f'/api/v1/parent_delete/{parent_create.id}/')

    assert response.status_code == 204
