from rest_framework import serializers
from src.apps.jounal.models import SubjectTeacher


class SubjectTeacherCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectTeacher
        fields = '__all__'

    def create(self, validated_data):
        return SubjectTeacher.objects.create(**validated_data)
