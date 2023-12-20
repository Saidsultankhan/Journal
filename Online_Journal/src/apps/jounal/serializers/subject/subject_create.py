from rest_framework import serializers
from src.apps.jounal.models import Subject


class SubjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)
