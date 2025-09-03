from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view

urlpatterns = [

    path('login/',  CustomLoginView.as_view(), name='login'),
    path('logout/',  logout_view, name='logout'),
    path('login/',  RegisterPage.as_view(), name='register'),



    path('',  views.index, name='index'),

    path('students/',  views.students, name='student_list'),
    path('display_students/',  views.display_students, name='display_students'),
    path('add_student/',  views.add_student, name='add_student'),
    path('edit_student/<int:pk>/',  views.edit_student, name='edit_student'),
    path('student/<int:pk>/',  views.student_detail, name='student_detail'),
    path('delete_student/<int:pk>/',  views.delete_student, name='delete_student'),
    path('print_students/',  views.print_students, name='print_students'),


    path('teachers/',  views.teachers, name='teachers_list'),
    path('display_teachers/',  views.display_teachers, name='display_teachers'),
    path('add_teacher/',  views.add_teacher, name='add_teacher'),


    path('subjects/',  views.subjects, name='subjects_list'),
    path('display_subjects/',  views.display_subjects, name='display_subjects'),
    path('add_subjects/',  views.add_subjects, name='add_subjects'),


    path('statements/',  views.statements, name='statements_list'),
    path('display_statements/',  views.display_statements, name='display_statements'),
    path('add_statement/',  views.add_statement, name='add_statement'),
    path('edit_student/<int:pk>/',  views.edit_student, name='edit_student'),
    path('statement/<int:pk>/',  views.statement_detail, name='statement_detail'),
    path('delete_statement/<int:pk>/',  views.delete_statements, name='delete_statement'),
    path('search/',  views.search_statements, name='search_statements'),
    path('print_statements/',  views.print_statements, name='print_statements'),
]