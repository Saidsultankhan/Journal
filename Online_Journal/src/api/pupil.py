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
        if self.action == 'retrieve':
            return PupilDetailSerializer
        elif self.action == 'list':
            return PupilListSerializer
        elif self.action == 'update':
            return PupilUpdateSerializer
        elif self.action == 'create':
            return PupilCreateSerializer
        elif self.action == 'delete':
            return PupilDeleteSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsTeacherOrPupilOrParentOrAdmin()]
        elif self.action == 'list':
            return [IsTeacherOrMentorOrAdmin()]
        elif self.action == 'create':
            return [IsAdminUser()]
        elif self.action == 'update':
            return [IsAdminUser()]
        return super().get_permissions()
