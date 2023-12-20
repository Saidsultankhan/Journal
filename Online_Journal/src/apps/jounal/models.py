from django.db import models
from django.contrib.auth.models import User
from .static_data import *


class Name(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_user')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Parent(Name):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent_user')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'


class Pupil(Name):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pupil_user')
    grade = models.ForeignKey('Class', related_name='class_pupil', on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('Parent', related_name='pupil_parent', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Pupil'
        verbose_name_plural = 'Pupils'


class DairyOfClass(models.Model):
    mark = models.PositiveSmallIntegerField(choices=MARK_CHOICES)
    pupil = models.ForeignKey(Pupil, on_delete=models.SET_NULL, related_name='dairy_pupil', null=True, blank=True)
    subject = models.ForeignKey('Subject', related_name='subject', on_delete=models.CASCADE)
    quarter = models.PositiveSmallIntegerField(choices=QUARTER_CHOICES)
    grade = models.ForeignKey(
        'Class',
        on_delete=models.SET_NULL,
        related_name='dairy_of_class',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.mark}'

    class Meta:
        verbose_name = 'DairyOfClass'
        verbose_name_plural = 'DairiesOfClass_class'


# class School(Name):
#
#     def __str__(self):
#         return self.name_en
#
#     class Meta:
#         verbose_name = 'School'
#         verbose_name_plural = 'Schools'


class Class(models.Model):
    number = models.SmallIntegerField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    # Should be OneToOneField instead of ForeignKey
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='class_teacher', null=True, blank=True)
    # school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school', null=True)

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
        unique_together = ('number', 'type')

    def __str__(self):
        return f'{self.number}{self.type}'


class Subject(Name):

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subject_teacher_teacher')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_teacher_subject')
    grade = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subject_teacher_class')

    def __str__(self):
        return f'{self.subject}-{self.teacher}'

    class Meta:
        verbose_name = 'Subject-Teacher'
        verbose_name_plural = 'Subjects-Teachers'
