from django.contrib import admin
from .models import *
from django.utils.html import format_html, mark_safe
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'show_photo')
    fields = ['surname', 'name', 'date_of_birth', ('group','photo','show_photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                f'<img src="{obj.photo.url}" style="max-height:100px;">')
        else:
            return "photo not found"
    show_photo.short_description = 'photo studenta'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'show_photo')
    fields = ['surname', 'name', ('photo','show_photo')]
    readonly_fields = ["show_photo"]



    def show_photo(self, obj):
        if obj.photo:
            return format_html(
                 f'<img src="{obj.photo.url}" style="max-height:100px;">')   
        
        else:
            return "photo not found"

    show_photo.short_description = 'photo prepoda'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'name')
    fields = ['surname', 'name']
    search_fields = ('name')
    list_filter = ('name', 'teacher')


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ('student', 'attendance', 'subject', 'grade', 'estimation', 'date_of_rating', 'teacher')
    search_fields = ('student__surname', 'subject__name', 'teacher__surname', 'date_of_racing')
    list_filter = ('attendance', 'subject', 'grade', 'estimation')