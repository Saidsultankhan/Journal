import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_teacher_create(
        request,
        client,
        status_code,
        payload,
        teachers_list,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    url = reverse('teacher-list')
    response = auth_client.get(url)

    assert response.status_code == status_code

    if payload == 'SUCCESS':
        assert len(response.data) == len(teachers_list)

    assert response.status_code == status_code
