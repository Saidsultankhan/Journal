from rest_framework import serializers
from src.apps.jounal.models import Pupil
from django.contrib.auth.models import User


class PupilUpdateSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(required=False)
    name_en = serializers.CharField(required=False)
    name_ru = serializers.CharField(required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

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