from rest_framework import viewsets
from src.apps.jounal.models import SubjectTeacher
from src.apps.jounal.serializers import (
    SubjectTeacherListSerializer,
    SubjectTeacherDetailSerializer,
    SubjectTeacherCreateSerializer,
    SubjectTeacherUpdateSerializer,
    SubjectTeacherDeleteSerializer
)
from src.apps.jounal.permissions import TeacherOrAdmin
from rest_framework.permissions import IsAdminUser


class SubjectTeacherViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacher.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'list':
            return SubjectTeacherListSerializer
        elif self.action == 'retrieve':
            return SubjectTeacherDetailSerializer
        elif self.action == 'create':
            return SubjectTeacherCreateSerializer
        elif self.action == 'update':
            return SubjectTeacherUpdateSerializer
        elif self.action == 'delete':
            return SubjectTeacherDeleteSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            # admin, teacher of this subject
            return [TeacherOrAdmin()]
        elif self.action == 'list':
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsAdminUser()]
        elif self.action == 'update':
            return [IsAdminUser()]
        return super().get_permissions()

