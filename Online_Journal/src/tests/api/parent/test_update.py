import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('admin_client', 404, "NOT_FOUND"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_parent_update(
        request,
        client,
        status_code,
        payload,
        parent_create,
        user_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]

    statuses = ['FORBIDDEN', 'NOT_FOUND', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}
    for status in statuses:
        datas[status] = {
            'name_uz': user_create.username,
            'name_ru': user_create.username,
            'name_en': user_create.username,
            'user': user_create.id
        }

    url = reverse('parent-detail', kwargs={'pk': parent_create.id})
    
    if payload == 'NOT_FOUND':
        url = reverse('parent-detail', kwargs={'pk': parent_create.id+1})

        response = auth_client.patch(url, datas[payload])
    else:
        response = auth_client.patch(url, datas[payload])

    assert response.status_code == status_code
