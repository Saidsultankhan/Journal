from rest_framework import serializers
from src.apps.jounal.models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id', 'name')

    def get_name(self, obj):
        return obj.user.username
