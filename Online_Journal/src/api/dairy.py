from rest_framework import viewsets
from src.apps.jounal.models import DairyOfClass
from src.apps.jounal.serializers import (
    DairyOfClassSerializer,
    DairyDetailSerializer,
    DairyCreateSerializer,
    DairyUpdateSerializer,
    DairyDeleteSerializer,
)
from src.apps.jounal.permissions import (
    IsTeacherOrMentorOrAdmin,
    TeacherOrAdmin,
    DairyTeacher
)
from rest_framework.permissions import IsAdminUser


class DairyViewSet(viewsets.ModelViewSet):
    queryset = DairyOfClass.objects.all()

    def get_serializer_class(self):
        serializers = {
            'retrieve': DairyDetailSerializer,
            'create': DairyCreateSerializer,
            'list': DairyOfClassSerializer,
            'delete': DairyDeleteSerializer,
            'update': DairyUpdateSerializer
        }
        return serializers.get(self.action)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [DairyTeacher]
        elif self.action == 'create':
            permission_classes = [DairyTeacher]
        elif self.action == 'update':
            permission_classes = [DairyTeacher]
        elif self.action == 'list':
            permission_classes = [DairyTeacher]

        return [permission_class() for permission_class in permission_classes]
