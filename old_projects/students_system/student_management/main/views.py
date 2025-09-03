from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from .models import Course, Schedule, Grade


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def is_student(user):
    return hasattr(user, 'student_profile')


def is_teacher(user):
    return hasattr(user, 'teacher_profile')


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'admin/dashboard.html')


@login_required
def teacher_dashboard(request):
    if not is_teacher(request.user):
        return redirect('home')

    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/dashboard.html', {'courses': courses})


@login_required
def teacher_schedule(request):
    if not is_teacher(request.user):
        return redirect('home')

    schedules = Schedule.objects.filter(course__teacher=request.user)
    return render(request, 'teacher/schedule.html', {'schedules': schedules})


@login_required
def teacher_gradebook(request):
    if not hasattr(request.user, 'teacher_profile'):
        return redirect('home')

    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/gradebook.html', {'courses': courses})


@login_required
def add_grade(request):
    if not hasattr(request.user, 'teacher_profile'):
        return redirect('home')

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        grade_value = request.POST.get('grade_value')
        comment = request.POST.get('comment', '')

        try:
            student = User.objects.get(id=student_id)
            course = Course.objects.get(id=course_id, teacher=request.user)

            Grade.objects.update_or_create(
                student=student,
                course=course,
                defaults={
                    'value': grade_value,
                    'comment': comment
                }
            )
            messages.success(request, 'Оценка успешно сохранена')
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')

        return redirect('teacher_gradebook')

    return redirect('teacher_gradebook')


@login_required
def student_dashboard(request):
    if not is_student(request.user):
        return redirect('home')
    return render(request, 'student/dashboard.html')


@register.filter
def filter_schedule(queryset, day):
    return queryset.filter(day=day)


@register.filter
def filter_time(queryset, time):
    return queryset.filter(start_time=time)


@login_required
def student_schedule(request):
    if not hasattr(request.user, 'student_profile'):
        return redirect('home')

    schedules = Schedule.objects.filter(
        course__grades__student=request.user
    ).select_related('course', 'course__teacher').order_by('day', 'start_time')

    time_slots = sorted({s.start_time.strftime('%H:%M') for s in schedules})
    day_codes = ['mon', 'tue', 'wed', 'thu', 'fri']

    return render(request, 'student/schedule.html', {
        'schedules': schedules,
        'time_slots': time_slots,
        'day_codes': day_codes
    })


@login_required
def student_grades(request):
    if not is_student(request.user):
        return redirect('home')

    grades = Grade.objects.filter(student=request.user)
    return render(request, 'student/grades.html', {'grades': grades})
