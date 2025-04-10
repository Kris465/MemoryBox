from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .mixins import StudentAuthMixin
from main.models import (
    Student, Schedule, Grade,
    Attendance, Course
)


class StudentLoginView(View):
    """Аутентификация студента"""
    template_name = 'student/login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'student':
            return redirect('student_dashboard')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.role == 'student':
            login(request, user)
            return redirect('student_dashboard')
        
        messages.error(request, 'Неверные учетные данные')
        return render(request, self.template_name)


class StudentLogoutView(View):
    """Выход из системы"""
    def get(self, request):
        logout(request)
        return redirect('student_login')


class StudentDashboardView(StudentAuthMixin, View):
    """Главная страница студента"""
    template_name = 'student/dashboard.html'

    def get(self, request):
        student = request.user.student_profile
        today = timezone.now().date()
        
        # Ближайшие занятия
        upcoming_schedules = Schedule.objects.filter(
            course__name=student.course,
            start_time__date__gte=today
        ).order_by('start_time')[:3]
        
        # Последние оценки
        recent_grades = Grade.objects.filter(
            student=student
        ).select_related('course').order_by('-date')[:5]
        
        context = {
            'student': student,
            'upcoming_schedules': upcoming_schedules,
            'recent_grades': recent_grades,
        }
        return render(request, self.template_name, context)


class StudentScheduleView(StudentAuthMixin, View):
    """Просмотр расписания"""
    template_name = 'student/schedule.html'

    def get(self, request):
        student = request.user.student_profile
        schedules = Schedule.objects.filter(
            course__name=student.course
        ).order_by('start_time')
        
        return render(request, self.template_name, {
            'schedules': schedules,
            'student': student
        })


class StudentGradesView(StudentAuthMixin, View):
    """Просмотр оценок"""
    template_name = 'student/grades.html'

    def get(self, request):
        student = request.user.student_profile
        grades = Grade.objects.filter(
            student=student
        ).select_related('course').order_by('-date')
        
        # Расчет среднего балла
        avg_grade = grades.aggregate(models.Avg('numeric_score'))['numeric_score__avg']
        
        return render(request, self.template_name, {
            'grades': grades,
            'student': student,
            'avg_grade': round(avg_grade, 2) if avg_grade else None
        })


class StudentAttendanceView(StudentAuthMixin, View):
    """Просмотр посещаемости"""
    template_name = 'student/attendance.html'

    def get(self, request):
        student = request.user.student_profile
        attendance = Attendance.objects.filter(
            student=student
        ).select_related('schedule', 'schedule__course')
        
        # Статистика посещаемости
        total_classes = attendance.count()
        present_count = attendance.filter(status='present').count()
        attendance_rate = (present_count / total_classes * 100) if total_classes > 0 else 0
        
        return render(request, self.template_name, {
            'attendance_records': attendance,
            'student': student,
            'attendance_rate': round(attendance_rate, 1),
            'total_classes': total_classes,
            'present_count': present_count
        })


class StudentSettingsView(StudentAuthMixin, View):
    """Настройки профиля"""
    template_name = 'student/settings.html'

    def get(self, request):
        student = request.user.student_profile
        return render(request, self.template_name, {'student': student})

    def post(self, request):
        student = request.user.student_profile
        user = request.user
        
        try:
            # Обновление пароля
            new_password = request.POST.get('new_password')
            if new_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Пароль успешно изменен')
            
            # Обновление контактных данных
            student.contact_num = request.POST.get('contact_num')
            student.save()
            
            messages.success(request, 'Настройки сохранены')
            return redirect('student_settings')
            
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
            return self.get(request)
