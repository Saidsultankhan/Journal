from rest_framework import serializers
from src.apps.jounal.models import Class, Teacher


class ClassUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        exclude = ('id',)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.type = validated_data.get('type', instance.type)
        teacher_id = validated_data.get('teacher')
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            instance.teacher = teacher
        instance.save(**validated_data)

        return instance