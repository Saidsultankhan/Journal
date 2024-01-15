import pytest
from rest_framework.test import APIClient
# from rest_framework import status
# from django.contrib.auth.models import User
# from src.apps.jounal.models import Teacher

api_client = APIClient()


@pytest.mark.django_db
def test_user_create():
    response = api_client.post('/auth/users/', data={
        'email': 'email_test@test.com',
        'username': 'username_1',
        'password': 'password_1',
        }
    )
    print(1)

    assert response.status_code == 201


@pytest.mark.django_db
def test_user_login(user_create):
    data = {
        'username': user_create.username,
        'password': '23456789',
    }
    response = api_client.post('/auth/token/login/', data)
    print(2)

    assert response.status_code == 200


@pytest.mark.django_db
def test_parent_create(parent_factory, user_create):
    data = {
        'name_uz': parent_factory.name_uz,
        'name_ru': parent_factory.name_ru,
        'name_en': parent_factory.name_en,
        'user': user_create.id
    }
    print(3)
    response = api_client.post('/api/v1/parent_create/', data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_parent_update(parent_create):
    data = {
        'name_uz': 'Sultan',
    }
    response = api_client.patch(f'/api/v1/parent_update/{parent_create.id}/', data)
    print('4')

    assert response.data['name_uz'] == 'Sultan'


@pytest.mark.django_db
def test_parent_delete(parent_create):
    response = api_client.delete(f'/api/v1/parent_delete/{parent_create.id}/')
    print(5)

    assert response.status_code == 204


@pytest.mark.django_db
def test_parent_list(parents_list):
    response = api_client.get(f'/api/v1/parents/')
    assert len(response.data) == 3


@pytest.mark.django_db
def test_parent_get(parent_create):
    response = api_client.get(f'/api/v1/parent_detail/{parent_create.id}/')

    assert response.data['user'] == parent_create.user.id


@pytest.mark.django_db
def test_teacher_create(admin_create):
    api_client.force_authenticate(user=admin_create)
    data = {
        'user': admin_create.id
    }
    response = api_client.post(f'/api/v1/teacher_create/', data)
    print(7)

    assert response.status_code == 201


@pytest.mark.django_db
def test_teacher_update(admin_create, teacher_create, user_create):
    api_client.force_authenticate(user=admin_create)
    if teacher_create.user.id != user_create.id:
        data = {
            'user': user_create.id
        }
    else:
        print("The users' ids' are the same")
    response = api_client.patch(f'/api/v1/teacher_update/{teacher_create.id}/', data)
    print(8)

    assert response.data['user'] == user_create.id


@pytest.mark.django_db
def test_teacher_delete(admin_create, teacher_create):
    api_client.force_authenticate(user=admin_create)
    response = api_client.delete(f'/api/v1/teacher_delete/{teacher_create.id}/')
    print(9)

    assert response.status_code == 204


@pytest.mark.django_db
def test_teacher_get(admin_create, teacher_create):
    api_client.force_authenticate(user=admin_create)
    response = api_client.get(f'/api/v1/teacher/{teacher_create.id}/')
    print(10)

    assert response.data['user'] == teacher_create.user.id


@pytest.mark.django_db
def test_teacher_list(admin_create, teachers_list):
    api_client.force_authenticate(user=admin_create)
    response = api_client.get(f'/api/v1/teachers/')
    print(11)

    assert len(response.data) == len(teachers_list)


@pytest.mark.django_db
def test_grade_create(admin_create, teacher_create):
    api_client.force_authenticate(user=admin_create)
    data = {
        'type': 'a',
        'number': 11,
        'mentor': teacher_create.id
    }
    response = api_client.post(f'/api/v1/class_create/', data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_grade_get(admin_create, grade_create):
    api_client.force_authenticate(user=admin_create)
    response = api_client.get(f'/api/v1/class/{grade_create.id}/')
    print(13)

    assert response.data['mentor']['id'] == grade_create.teacher.id


@pytest.mark.django_db
def test_grade_list(admin_create, grades_list):
    api_client.force_authenticate(user=admin_create)
    response = api_client.get(f'/api/v1/classes/')
    print(14)

    assert len(response.data) == len(grades_list)


# @pytest.mark.django_db
# def test_grade_update(admin_create, grade_create):
#     api_client.force_authenticate(user=admin_create)
#
#     data = {
#         'type': 'a',
#         'number': 11
#     }
#     response = api_client.patch(f'/api/v1/class_update/{grade_create.id}/', data)
#     print(response)
#     # assert response.data['type'] == 'a'
