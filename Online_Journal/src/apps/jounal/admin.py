from django.contrib import admin
from .models import *

admin.site.register(Parent)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz']


@admin.register(SubjectTeacher)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'grade', 'subject', 'name']

    def name(self, obj):
        return str(obj)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade', 'teacher', 'id']

    def grade(self, obj):
        return str(obj)


@admin.register(Teacher)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(DairyOfClass)
class DairyAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark']


@admin.register(Pupil)
class DairyAdmin(admin.ModelAdmin):
    list_display = ['id', 'grade', 'parent', 'name_uz']
