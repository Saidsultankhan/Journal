from rest_framework.test import APIClient
import pytest
# from src.apps.jounal.models import *

# @pytest.mark.django_db
# class TestClassViewSet:
#
#     @pytest.fixture
#     def users_tests(self):
#         return Class.objects.create(name='Test Class', description='Test Description')
#
#     def test_retrieve_class(self, sample_class):
#         client = APIClient()
#         response = client.get(f'/api/v1/class/<int:pk>/{users_tests.id}/')
#         assert response.status_code == 200
#
#     def test_create_class(self):
#         client = APIClient()
#         data = {'name': 'New Class', 'description': 'New Description'}
#         response = client.post('/api/v1/class_create/', data)
#         assert response.status_code == 201
#
#     def test_update_class(self, obj):
#         client = APIClient()
#         data = {'name': 'Updated Class Name', 'description': 'Updated Description'}
#         response = client.patch(f'/api/v1/class_update/<int:pk>/{users_tests.id}/', data)
#         assert response.status_code == 200
#
#     def test_list_class(self):
#         client = APIClient()
#         response = client.get('/api/v1/classes/')
#         assert response.status_code == 200



