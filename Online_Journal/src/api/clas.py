from rest_framework import viewsets
from src.apps.jounal.models import Class
from src.apps.jounal.serializers import (
    ClassDetailSerializer,
    ClassListSerializer,
    ClassCreateSerializer,
    ClassUpdateSerializer,
    ClassDeleteSerializer,
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin
from rest_framework.permissions import IsAdminUser


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassUpdateSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassDetailSerializer
        elif self.action == 'create':
            return ClassCreateSerializer
        elif self.action == 'list':
            return ClassListSerializer
        elif self.action == 'delete':
            return ClassDeleteSerializer
        elif self.action == 'update':
            return ClassUpdateSerializer
        return super().get_serializer_class()

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
