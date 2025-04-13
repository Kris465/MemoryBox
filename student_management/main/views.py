from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course, Schedule, Grade


# Проверки ролей
def is_teacher(user):
    return hasattr(user, 'teacher_profile')


def is_student(user):
    return hasattr(user, 'student_profile')


# Основные страницы
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# Админка
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


# Преподаватели
@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/dashboard.html', {'courses': courses})


@login_required
@user_passes_test(is_teacher)
def teacher_schedule(request):
    schedules = Schedule.objects.filter(course__teacher=request.user)
    return render(request, 'teacher/schedule.html', {'schedules': schedules})


@login_required
@user_passes_test(is_teacher)
def gradebook(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/gradebook.html', {'courses': courses})


# Студенты
@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'student/dashboard.html')


@login_required
@user_passes_test(is_student)
def student_schedule(request):
    schedules = Schedule.objects.filter(course__grade__student=request.user)
    return render(request, 'student/schedule.html', {'schedules': schedules})


@login_required
@user_passes_test(is_student)
def student_grades(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'student/grades.html', {'grades': grades})
