from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['surname', 'name', 'date_of_birth', 'group', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['student', 'subject', 'attendance', 'grade', 'estimation', 'date_of_rating', 'teacher']
        widgets = {
            'date_of_rating': forms.DateInput(attrs={'type': 'date'}),
        }
