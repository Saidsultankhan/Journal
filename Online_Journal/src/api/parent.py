from rest_framework import viewsets
from src.apps.jounal.models import Parent
from src.apps.jounal.serializers.parent import (
    ParentCreateUpdateDeleteSerializer,
    ParentDetailSerializer
)


class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()

    def get_serializer_class(self):
        serializers = {
            'retrieve': ParentDetailSerializer,
            'create': ParentCreateUpdateDeleteSerializer,
            'update': ParentCreateUpdateDeleteSerializer,
            'delete': ParentCreateUpdateDeleteSerializer,
            # 'list': ClassListSerializer,

        }
        return serializers.get(self.action)

    # def get_permissions(self):
    #     permission_classes = []
        # if self.action == 'retrieve':
            # permission_classes = [IsTeacherOrMentorOrAdmin]
        # elif self.action == 'create':
        #     permission_classes = [IsAdminUser]
        # elif self.action == 'update':
            # permission_classes = [IsAdminUser]
        # elif self.action == 'list':
        #     permission_classes = [IsAdminUser]
        # return [permission_class() for permission_class in permission_classes]