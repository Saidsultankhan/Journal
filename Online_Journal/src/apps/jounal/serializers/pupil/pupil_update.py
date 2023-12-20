from rest_framework import serializers
from src.apps.jounal.models import Pupil


class PupilUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name_uz = validated_data.get('name_uz', instance.name_uz)
        instance.name_ru = validated_data.get('name_ru', instance.name_ru)
        instance.name_en = validated_data.get('name_en', instance.name_en)
        instance.user = validated_data.get('user', instance.user)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()
        return instance