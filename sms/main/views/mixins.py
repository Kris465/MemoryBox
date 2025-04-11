from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class StudentRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'student'

    def handle_no_permission(self):
        messages.error(self.request, 'Требуется авторизация студента')
        return redirect('student_login')


class TeacherRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'teacher'

    def handle_no_permission(self):
        messages.error(self.request, 'Требуется авторизация преподавателя')
        return redirect('teacher_login')


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'Требуются права администратора')
        return redirect('admin:login')
