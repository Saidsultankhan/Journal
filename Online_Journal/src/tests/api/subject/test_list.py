import pytest


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('admin_client', 200, "SUCCESS"),
    ]
)
@pytest.mark.django_db
def test_subject_get(
        request,
        client,
        status_code,
        payload,
        subjects_list,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    response = auth_client.get(f'/api/v1/subjects/')

    if payload == 'SUCCESS':
        assert len(response.data) == len(subjects_list)

    assert response.status_code == status_code
