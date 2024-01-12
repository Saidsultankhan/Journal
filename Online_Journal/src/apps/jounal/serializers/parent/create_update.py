from rest_framework import serializers
from src.apps.jounal.models import Parent
from django.contrib.auth.models import User


class ParentCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    name_uz = serializers.CharField(required=False)
    name_en = serializers.CharField(required=False)
    name_ru = serializers.CharField(required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Parent
        fields = '__all__'

    # def create(self, validated_data):
    #     return Parent.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name_uz = validated_data.get('name_uz', instance.name_uz)
    #     instance.name_ru = validated_data.get('name_ru', instance.name_ru)
    #     instance.name_en = validated_data.get('name_en', instance.name_en)
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.save()
    #     return instance