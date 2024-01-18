
import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_parent_create(parent_factory, user_create):
    data = {
        'name_uz': parent_factory.name_uz,
        'name_ru': parent_factory.name_ru,
        'name_en': parent_factory.name_en,
        'user': user_create.id
    }
    response = api_client.post('/api/v1/parent_create/', data)

    assert response.status_code == 201
