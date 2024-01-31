from rest_framework import viewsets
from src.apps.jounal.models import Parent
from src.apps.jounal.serializers.parent import (
    ParentCreateUpdateDeleteListSerializer,
    ParentDetailSerializer
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)
from src.apps.jounal.permissions import IsTeacherOrMentorOrAdmin


class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()

    def get_serializer_class(self):
        serializers = {
            'retrieve': ParentDetailSerializer,
            'create': ParentCreateUpdateDeleteListSerializer,
            'partial_update': ParentCreateUpdateDeleteListSerializer,
            'delete': ParentCreateUpdateDeleteListSerializer,
            'list': ParentCreateUpdateDeleteListSerializer,

        }
        return serializers.get(self.action, ParentDetailSerializer)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsAdminUser or IsTeacherOrMentorOrAdmin]
        elif self.action in ['create', 'partial_update', 'list', 'destroy']:
            permission_classes = [IsAdminUser]

        return [permission_class() for permission_class in permission_classes]
