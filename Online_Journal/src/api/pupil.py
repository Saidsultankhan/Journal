from rest_framework import viewsets
from src.apps.jounal.models import Pupil
from src.apps.jounal.serializers import (
    PupilDetailSerializer,
    PupilListSerializer,
    PupilUpdateSerializer,
    PupilCreateSerializer,
    PupilDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin, IsTeacherOrPupilOrParentOrAdmin
from rest_framework.permissions import IsAdminUser


class PupilsViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()

    def get_serializer_class(self):
        serializers = {
            'retrieve': PupilDetailSerializer,
            'list': PupilListSerializer,
            'update': PupilUpdateSerializer,
            'create': PupilCreateSerializer,
            'delete': PupilDeleteSerializer,
        }
        return serializers.get(self.action)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [IsTeacherOrPupilOrParentOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsTeacherOrMentorOrAdmin]
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAdminUser]

        return [permission_class() for permission_class in permission_classes]
