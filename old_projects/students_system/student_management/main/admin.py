from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Course, Schedule, Grade, StudentProfile, TeacherProfile


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'teacher')
    list_filter = ('start_date', 'teacher')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'get_day_display', 'start_time', 'end_time')
    list_filter = ('day', 'course')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'get_value_display', 'date')
    list_filter = ('course', 'date')


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'get_role')

    def get_role(self, obj):
        if hasattr(obj, 'teacher_profile'):
            return "Преподаватель"
        elif hasattr(obj, 'student_profile'):
            return "Студент"
        return "Администратор"
    get_role.short_description = 'Роль'
