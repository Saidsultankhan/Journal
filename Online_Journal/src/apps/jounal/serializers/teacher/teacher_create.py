from rest_framework import serializers
from src.apps.jounal.models import Teacher


class TeacherCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
