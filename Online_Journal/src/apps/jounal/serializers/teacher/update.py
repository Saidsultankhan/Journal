from rest_framework import serializers
from src.apps.jounal.models import Teacher


class TeacherUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def update(self, instance, validated_data):
        user = validated_data.get('user', instance.user)
        instance.user = user
        instance.save()
        return instance
