from rest_framework import viewsets
from src.apps.jounal.models import Grade
from src.apps.jounal.serializers import (
    GradeDetailSerializer,
    GradeListSerializer,
    GradeCreateSerializer,
    GradeUpdateSerializer,
    GradeDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin
from rest_framework.permissions import IsAdminUser


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()

    def get_serializer_class(self):
        serializers = {
            'retrieve': GradeDetailSerializer,
            'create': GradeCreateSerializer,
            'list': GradeListSerializer,
            'delete': GradeDeleteSerializer,
            'update': GradeUpdateSerializer
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
