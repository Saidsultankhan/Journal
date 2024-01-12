from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass, SubjectTeacher


class DairyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DairyOfClass
        fields = ('mark', 'quarter', 'pupil', 'subject')

    def create(self, validated_data):
        teacher = self.context['request'].user.teacher_user.first()
        if teacher:
            subject = validated_data.get('subject')
            grade = validated_data.get('pupil').grade.id
            if SubjectTeacher.objects.filter(teacher=teacher, subject=subject, grade=grade).exists():
                return DairyOfClass.objects.create(**validated_data)
        raise serializers.ValidationError("У вас нет прав для добавления оценок в этот класс или по данному предмету.")

