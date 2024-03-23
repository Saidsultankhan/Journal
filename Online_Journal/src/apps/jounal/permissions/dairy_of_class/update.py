from rest_framework import permissions


class DairyTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        print(1)
        if request.user.is_authenticated:
            return True
        

    def has_object_permission(self, request, view, obj):
        print('adasdasdasdasd')
        return (
                request.user.is_authenticated and
                (request.user.is_staff or obj.subject.subject_teacher_subject.filter(
                    teacher__user=request.user,
                    grade=obj.grade).exists()
                 )
        )


class DairyListTeacher(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.teacher_user.first() or request.user.is_staff:
            return True
