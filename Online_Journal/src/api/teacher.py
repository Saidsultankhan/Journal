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
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)


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
            permission_classes = [IsAuthenticated and IsAdminUser, IsTeacherOrMentorOrAdmin]
        elif self.action in ['create', 'update', 'list', 'destroy']:
            permission_classes = [IsAdminUser]

        return [permission_class() for permission_class in permission_classes]
