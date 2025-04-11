from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (User, Grade, Course, Student, Teacher, Schedule,
                     Attendance, AboutPage, ContactPage)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'phone')}),
    )


admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(Attendance)
