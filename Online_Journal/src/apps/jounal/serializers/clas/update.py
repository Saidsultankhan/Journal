from rest_framework import serializers
from src.apps.jounal.models import Grade, Teacher


class GradeUpdateSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=False)
    type = serializers.CharField(required=False)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False)

    class Meta:
        model = Grade
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.type = validated_data.get('type', instance.type)
        teacher_id = validated_data.get('teacher')
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id.id)
            instance.teacher = teacher_id
        instance.save()

        return instance