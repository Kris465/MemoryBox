from django.contrib import admin
from .models import AboutPage, main_grade, Course, ContactPage, Student, Notice, Teacher

# Register your models here.
admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(main_grade)
admin.site.register(Notice)
admin.site.register(Teacher)
