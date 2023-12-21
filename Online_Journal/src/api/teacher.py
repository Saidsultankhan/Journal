from rest_framework import viewsets
from src.apps.jounal.models import Teacher
from src.apps.jounal.serializers import (
    TeacherCreateSerializer,
    TeacherDetailSerializer,
    TeacherListSerializer,
    TeacherUpdateSerializer,
    TeacherDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin
from rest_framework.permissions import IsAdminUser


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        serializers = {
            'list': TeacherListSerializer,
            'retrieve': TeacherDetailSerializer,
            'create': TeacherCreateSerializer,
            'update': TeacherUpdateSerializer,
            'delete': TeacherDeleteSerializer
        }
        return serializers.get(self.action)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [IsTeacherOrMentorOrAdmin]
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission_class() for permission_class in permission_classes]
