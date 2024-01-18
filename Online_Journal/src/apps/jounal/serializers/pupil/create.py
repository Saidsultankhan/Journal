from rest_framework import serializers
from src.apps.jounal.models import Pupil, Teacher


class PupilCreateSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(required=False)
    name_en = serializers.CharField(required=False)
    name_ru = serializers.CharField(required=False)

    class Meta:
        model = Pupil
        fields = '__all__'

    def create(self, validated_data):
        return Pupil.objects.create(**validated_data)
