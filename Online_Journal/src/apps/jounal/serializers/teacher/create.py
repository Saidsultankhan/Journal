from rest_framework import serializers
from src.apps.jounal.models import Teacher
from django.contrib.auth.models import User



class TeacherCreateSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
