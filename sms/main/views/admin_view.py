from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from ..models import Student, Teacher, Course


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class AdminDashboardView(LoginRequiredMixin, AdminRequiredMixin, View):
    template_name = 'admin/dashboard.html'

    def get(self, request):
        context = {
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'courses_count': Course.objects.count()
        }
        return render(request, self.template_name, context)