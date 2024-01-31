import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 204, "SUCCESS"),
        ('admin_client', 404, "NOT_FOUND"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_teacher_create(
        request,
        client,
        status_code,
        payload,
        teacher_create,
        user_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    url = reverse('teacher-detail', kwargs={'pk': teacher_create.id})
    response = auth_client.delete(url)

    if payload == 'NOT_FOUND':
        url = reverse('teacher-detail', kwargs={'pk': teacher_create.id+1})
        response = auth_client.delete(url)

    assert response.status_code == status_code

