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
        if self.action == 'list':
            return TeacherListSerializer
        elif self.action == 'retrieve':
            return TeacherDetailSerializer
        elif self.action == 'create':
            return TeacherCreateSerializer
        elif self.action == 'update':
            return TeacherUpdateSerializer
        elif self.action == 'delete':
            return TeacherDeleteSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            # mentor klassa ili prepod opr predmeta
            return [IsTeacherOrMentorOrAdmin()]
        elif self.action == 'create':
            return [IsAdminUser()]
        elif self.action == 'update':
            return [IsAdminUser()]
        elif self.action == 'list':
            return [IsAdminUser()]
        return super().get_permissions()
