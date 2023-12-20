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
        if self.action == 'list':
            return SubjectListSerializer
        elif self.action == 'retrieve':
            return SubjectDetailSerializer
        elif self.action == 'create':
            return SubjectCreateSerializer
        elif self.action == 'update':
            return SubjectUpdateSerializer
        elif self.action == 'delete':
            return SubjectDeleteSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            # admin, teacher of this subject
            return [TeacherOrAdmin()]
        elif self.action == 'list':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAdminUser()]
        elif self.action == 'update':
            return [IsAdminUser()]
        return super().get_permissions()
