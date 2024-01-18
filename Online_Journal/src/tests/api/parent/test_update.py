import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_parent_update(parent_create):
    data = {
        'name_uz': 'Sultan',
    }
    response = api_client.patch(f'/api/v1/parent_update/{parent_create.id}/', data)

    assert response.data['name_uz'] == 'Sultan'
