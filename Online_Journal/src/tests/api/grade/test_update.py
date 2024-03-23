import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('admin_client', 400, "BAD_REQUEST"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_grade_update(
        request,
        client,
        status_code,
        payload,
        admin_create,
        teacher_create,
        grade_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]

    statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}
    number = 11

    for status in statuses:
        datas[status] = {
            'number': number,
            'teacher': teacher_create.id
        }
        number -= 1
        if status == 'BAD_REQUEST':
            datas[status]['teacher'] = 1000
    url = reverse('grade-detail', kwargs={'pk': grade_create.id})
    response = auth_client.patch(url, datas[payload])

    assert response.status_code == status_code
    