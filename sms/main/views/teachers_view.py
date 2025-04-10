from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.db.models import Q
from datetime import date
from .mixins import TeacherAuthMixin
from main.models import (
    Schedule, Grade, Attendance,
    Student, Course
)


class TeacherLoginView(View):
    template_name = 'teacher/login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'teacher':
            return redirect('teacher_dashboard')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'teacher':
            login(request, user)
            return redirect('teacher_dashboard')

        messages.error(request, 'Неверные учетные данные')
        return render(request, self.template_name)


class TeacherDashboardView(TeacherAuthMixin, View):
    """Дашборд преподавателя"""
    template_name = 'teacher/dashboard.html'

    def get(self, request):
        teacher = request.user.teacher_profile
        today = date.today()

        upcoming_schedules = Schedule.objects.filter(
            teacher=teacher,
            start_time__date__gte=today
        ).order_by('start_time')[:5]

        recent_grades = Grade.objects.filter(
            teacher=teacher
        ).select_related('student', 'course').order_by('-date')[:5]

        context = {
            'upcoming_schedules': upcoming_schedules,
            'recent_grades': recent_grades,
            'courses': Course.objects.filter(teacher=teacher)
        }
        return render(request, self.template_name, context)


class TeacherScheduleView(TeacherAuthMixin, View):
    """Просмотр расписания преподавателя"""
    template_name = 'teacher/schedule.html'

    def get(self, request):
        teacher = request.user.teacher_profile
        schedules = Schedule.objects.filter(
            teacher=teacher
        ).order_by('start_time')

        return render(request, self.template_name, {
            'schedules': schedules
        })


class GradeBookView(TeacherAuthMixin, View):
    """Журнал оценок по курсу"""
    template_name = 'teacher/gradebook.html'

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher_profile)
        students = Student.objects.filter(course=course.name)
        grades = Grade.objects.filter(course=course).select_related('student')

        return render(request, self.template_name, {
            'course': course,
            'students': students,
            'grades': grades
        })


class AddGradeView(TeacherAuthMixin, View):
    """Добавление оценки"""
    template_name = 'teacher/add_grade.html'

    def get(self, request):
        teacher = request.user.teacher_profile
        courses = Course.objects.filter(teacher=teacher)
        students = Student.objects.filter(
            course__in=courses.values_list('name', flat=True)
        )

        return render(request, self.template_name, {
            'courses': courses,
            'students': students
        })

    def post(self, request):
        try:
            student = get_object_or_404(Student, id=request.POST.get('student'))
            course = get_object_or_404(Course, id=request.POST.get('course'))

            Grade.objects.create(
                student=student,
                course=course,
                teacher=request.user.teacher_profile,
                date=request.POST.get('date'),
                numeric_score=request.POST.get('score'),
                letter_grade=''
            )

            messages.success(request, 'Оценка успешно добавлена')
            return redirect('teacher_gradebook', course_id=course.id)

        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
            return self.get(request)


class AttendanceView(TeacherAuthMixin, View):
    """Управление посещаемостью"""
    template_name = 'teacher/attendance.html'

    def get(self, request, schedule_id):
        schedule = get_object_or_404(Schedule, id=schedule_id)
        students = Student.objects.filter(course=schedule.course.name)
        attendance_records = Attendance.objects.filter(
            schedule=schedule
        ).select_related('student')

        attendance_status = {
            record.student.id: record.status 
            for record in attendance_records
        }

        return render(request, self.template_name, {
            'schedule': schedule,
            'students': students,
            'attendance_status': attendance_status
        })

    def post(self, request, schedule_id):
        schedule = get_object_or_404(Schedule, id=schedule_id)
        students = Student.objects.filter(course=schedule.course.name)

        try:
            for student in students:
                status = request.POST.get(f'status_{student.id}', 'absent')

                Attendance.objects.update_or_create(
                    student=student,
                    schedule=schedule,
                    date=schedule.start_time.date(),
                    defaults={'status': status}
                )

            messages.success(request, 'Посещаемость сохранена')
            return redirect('teacher_schedule')

        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
            return self.get(request, schedule_id)
