from rest_framework import viewsets
from src.apps.jounal.models import Subject
from src.apps.jounal.serializers import (
    SubjectListSerializer,
    SubjectDetailSerializer,
    SubjectCreateSerializer,
    SubjectUpdateSerializer,
    SubjectDeleteSerializer,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser)
from src.apps.jounal.permissions.subject import TeacherOrAdmin


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()

    def get_serializer_class(self):
        serializers = {
            'list': SubjectListSerializer,
            'retrieve': SubjectDetailSerializer,
            'create': SubjectCreateSerializer,
            'update': SubjectUpdateSerializer,
            'delete': SubjectDeleteSerializer
        }
        return serializers.get(self.action)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [TeacherOrAdmin]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAdminUser]

        return [permission_class() for permission_class in permission_classes]
