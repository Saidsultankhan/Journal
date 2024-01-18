from rest_framework import serializers
from src.apps.jounal.models import Subject


class SubjectUpdateSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(required=False)
    name_en = serializers.CharField(required=False)
    name_ru = serializers.CharField(required=False)

    class Meta:
        model = Subject
        fields = ('name_uz', 'name_ru', 'name_en')

    def update(self, instance, validated_data):
        instance.name_uz = validated_data.get('name_uz', instance.name_uz)
        instance.name_ru = validated_data.get('name_ru', instance.name_ru)
        instance.name_en = validated_data.get('name_en', instance.name_en)
        instance.save()
        return instance