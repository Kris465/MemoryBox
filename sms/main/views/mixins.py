from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


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
        if not request.session.get('admin_authenticated'):
            messages.error(request, 'Пожалуйста, войдите как администратор')
            login_url = reverse('admin_login') + f"?next={request.path}"
            return HttpResponseRedirect(login_url)
        return super().dispatch(request, *args, **kwargs)
