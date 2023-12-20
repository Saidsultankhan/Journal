from rest_framework import serializers
from src.apps.jounal.models import Class, Teacher


class ClassCreateSerializer(serializers.ModelSerializer):
    mentor = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all())

    class Meta:
        model = Class
        fields = ('number', 'type', 'mentor')

    def create(self, validated_data):
        mentor = validated_data.pop('teacher')
        print(mentor)
        new_class = Class.objects.create(teacher=mentor, **validated_data)
        return new_class
