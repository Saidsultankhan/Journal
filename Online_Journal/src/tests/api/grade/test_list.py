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
def test_grade_list(
        request,
        client,
        status_code,
        payload,
        grades_list
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]
    url = reverse('grade-list')
    
    response = auth_client.get(url)

    if payload == 'SUCCESS':
        assert len(response.data) == len(grades_list)

    assert response.status_code == status_code

