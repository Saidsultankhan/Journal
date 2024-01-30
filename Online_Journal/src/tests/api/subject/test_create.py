import pytest


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
def test_subject_create(
        request,
        client,
        status_code,
        payload
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}

    for status in statuses:
        datas[status] = {
            'name_uz': 'Subject',
            'name_en': 'Subject1',
            'name_ru': 'Subject2',
        }

        if status == 'BAD_REQUEST':
            datas[status]['name_ru'] = ''

    response = auth_client.post(f'/api/v1/subject_create/', datas[payload])

    if payload == 'SUCCESS':
        assert response.data['name_uz'] == 'Subject'
        assert response.data['name_en'] == 'Subject1'
        assert response.data['name_ru'] == 'Subject2'

    assert response.status_code == status_code
