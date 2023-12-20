from rest_framework import serializers
from src.apps.jounal.models import Class


class ClassDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

    def delete(self, instance):
        instance.delete()
