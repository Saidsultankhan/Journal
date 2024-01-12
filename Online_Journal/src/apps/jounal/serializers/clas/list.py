from rest_framework import serializers
from src.apps.jounal.models import Grade


class GradeListSerializer(serializers.ModelSerializer):
    mentor = serializers.SerializerMethodField(source='teacher')
    name = serializers.CharField(source='__str__')
    pupils_number = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ('id', 'mentor', 'name', 'pupils_number')

    def get_pupils_number(self, obj):
        return obj.class_pupil.count()

    def get_mentor(self, obj):
        return obj.teacher.user.username
