from rest_framework import viewsets
from src.apps.jounal.models import DairyOfClass
from src.apps.jounal.serializers import (
    DairyOfClassSerializer,
    DairyDetailSerializer,
    DairyCreateSerializer,
    DairyUpdateSerializer,
    DairyDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin, TeacherOrAdmin
from rest_framework.permissions import IsAdminUser


class DairyViewSet(viewsets.ModelViewSet):
    queryset = DairyOfClass.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return DairyOfClassSerializer
        elif self.action == 'retrieve':
            return DairyDetailSerializer
        elif self.action == 'create':
            return DairyCreateSerializer
        elif self.action == 'update':
            return DairyUpdateSerializer
        elif self.action == 'delete':
            return DairyDeleteSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            # mentor klassa ili prepod opr predmeta
            return [IsTeacherOrMentorOrAdmin()]
        elif self.action == 'create':
            return [TeacherOrAdmin()]
        elif self.action == 'update':
            return [IsAdminUser()]
        elif self.action == 'list':
            return [IsTeacherOrMentorOrAdmin()]
        return super().get_permissions()
