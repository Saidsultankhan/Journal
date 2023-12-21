from rest_framework import viewsets
from src.apps.jounal.models import Class
from src.apps.jounal.serializers import (
    ClassDetailSerializer,
    ClassListSerializer,
    ClassCreateSerializer,
    ClassUpdateSerializer,
    ClassDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin
from rest_framework.permissions import IsAdminUser


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassUpdateSerializer

    def get_serializer_class(self):
        serializers = {
            'retrieve': ClassDetailSerializer,
            'create': ClassCreateSerializer,
            'list': ClassListSerializer,
            'delete': ClassDeleteSerializer,
            'update': ClassUpdateSerializer
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
