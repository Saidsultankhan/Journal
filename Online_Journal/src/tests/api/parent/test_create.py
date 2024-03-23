import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 201, "SUCCESS"),
        ('admin_client', 400, "BAD_REQUEST"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_parent_create(
        request,
        client,
        status_code,
        payload,
        parent_factory,
        user_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]

    statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}
    number = 1
    for status in statuses:
        datas[status] = {
            'name_uz': parent_factory.name_uz,
            'name_ru': parent_factory.name_ru,
            'name_en': parent_factory.name_en,
            'user': user_create.id
        }
        number += 1
        if status == 'BAD_REQUEST':
            datas[status]['user'] = 1000

    url = reverse('parent-list')
    response = auth_client.post(url, datas[payload])

    assert response.status_code == status_code
