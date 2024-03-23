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
def test_subject_teacher_get(
        request,
        client,
        status_code,
        payload,
        subject_teacher_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    url = reverse('subjectteacher-detail', kwargs={'pk': subject_teacher_create.id})
    
    if payload == 'NOT_FOUND':
        url = reverse('subjectteacher-detail', kwargs={'pk': subject_teacher_create.id+1})
        response = auth_client.get(url)
    else:
        response = auth_client.get(url)

    assert response.status_code == status_code

    if payload == 'SUCCESS':
        assert response.status_code == status_code
    