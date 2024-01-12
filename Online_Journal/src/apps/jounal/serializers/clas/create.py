from rest_framework import serializers
from src.apps.jounal.models import Grade, Teacher


class GradeCreateSerializer(serializers.ModelSerializer):
    mentor = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all())

    class Meta:
        model = Grade
        fields = ('number', 'type', 'mentor')

    def create(self, validated_data):
        mentor = validated_data.pop('teacher')
        print(mentor)
        new_class = Grade.objects.create(teacher=mentor, **validated_data)
        return new_class
