from rest_framework import viewsets
from src.apps.jounal.models import Grade
from src.apps.jounal.serializers import (
    GradeDetailSerializer,
    GradeListSerializer,
    GradeCreateSerializer,
    GradeUpdateSerializer,
    GradeDeleteSerializer,
)
from django.urls import reverse
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
            'partial_update': GradeUpdateSerializer
        }
        return serializers.get(self.action, GradeDetailSerializer)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [IsTeacherOrMentorOrAdmin]
        elif self.action in ['create', 'partial_update', 'list', 'destroy']:
            permission_classes = [IsAdminUser]
        return [permission_class() for permission_class in permission_classes]
