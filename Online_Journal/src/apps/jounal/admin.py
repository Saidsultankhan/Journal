from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)
admin.site.register(Parent)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['grade', 'teacher', 'id']

    def grade(self, obj):
        return str(obj)


@admin.register(DairyOfClass)
class DairyAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark']


@admin.register(Pupil)
class DairyAdmin(admin.ModelAdmin):
    list_display = ['id', 'grade', 'parent', 'name_uz']
