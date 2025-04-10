from django.shortcuts import redirect
from django.contrib import messages


class StudentAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('student_user'):
            messages.error(request, 'Войдите в систему как студент')
            return redirect('student_login')
        return super().dispatch(request, *args, **kwargs)


class TeacherAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('teacher_user'):
            return redirect('teacher_login')
        return super().dispatch(request, *args, **kwargs)


class AdminAuthMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('admin_user'):
            return redirect('admin_login')
        return super().dispatch(request, *args, **kwargs)
