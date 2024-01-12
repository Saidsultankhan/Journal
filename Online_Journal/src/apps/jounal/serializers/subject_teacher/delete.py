
from rest_framework import serializers
from src.apps.jounal.models import SubjectTeacher


class SubjectTeacherDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectTeacher
        fields = '__all__'

    def delete(self, instance):
        instance.delete()
