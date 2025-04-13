# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Основные страницы
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),
         name='logout'),

    # Админка (используем встроенную Django admin)
    path('admin/', views.admin_dashboard, name='admin_dashboard'),

    # Преподаватели
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/schedule/', views.teacher_schedule, name='teacher_schedule'),
    path('teacher/grades/', views.teacher_gradebook, name='teacher_gradebook'),
    path('teacher/grades/add/', views.add_grade, name='teacher_add_grade'),

    # Студенты
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('student/schedule/', views.student_schedule, name='student_schedule'),
    path('student/grades/', views.student_grades, name='student_grades'),
]
