from rest_framework import viewsets
from src.apps.jounal.models import SubjectTeacher
from src.apps.jounal.serializers import (
    SubjectTeacherListSerializer,
    SubjectTeacherDetailSerializer,
    SubjectTeacherCreateSerializer,
    SubjectTeacherUpdateSerializer,
    SubjectTeacherDeleteSerializer
)
from rest_framework.permissions import IsAdminUser


class SubjectTeacherViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacher.objects.all().order_by('id')

    def get_serializer_class(self):
        serializers = {
            'list': SubjectTeacherListSerializer,
            'retrieve': SubjectTeacherDetailSerializer,
            'create': SubjectTeacherCreateSerializer,
            'partial_update': SubjectTeacherUpdateSerializer,
            'delete': SubjectTeacherDeleteSerializer
        }
        return serializers.get(self.action, SubjectTeacherDetailSerializer)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        elif self.action in ['list', 'create', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]

        return [permission_class() for permission_class in permission_classes]
