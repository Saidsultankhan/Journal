from rest_framework import serializers
from src.apps.jounal.models import Teacher


class TeacherDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def delete(self, instance):
        instance.delete()