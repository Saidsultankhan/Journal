from rest_framework import serializers
from src.apps.jounal.models import SubjectTeacher


class SubjectTeacherUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectTeacher
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance