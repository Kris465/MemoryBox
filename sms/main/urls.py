from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views.students_view import (
    StudentLoginView, StudentLogoutView,
    StudentDashboardView, StudentScheduleView,
    StudentGradesView, StudentAttendanceView,
    StudentSettingsView
)
from .views.teachers_view import (
    TeacherDashboardView, TeacherScheduleView,
    GradeBookView, AddGradeView, AttendanceView,
    TeacherLoginView
)
from .views.common_views import HomeView, AboutView, ContactView
from .views.admin_view import AdminDashboardView

urlpatterns = [
    # Основные страницы
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),

    # Админка
    path('admin/dashboard/', AdminDashboardView.as_view(),
         name='admin_dashboard'),

    # Преподаватели
    path('teacher/login/', TeacherLoginView.as_view(), name='teacher_login'),
    path('teacher/dashboard/', TeacherDashboardView.as_view(),
         name='teacher_dashboard'),
    path('teacher/schedule/', TeacherScheduleView.as_view(),
         name='teacher_schedule'),
    path('teacher/grades/<int:course_id>/', GradeBookView.as_view(),
         name='teacher_gradebook'),
    path('teacher/grades/add/', AddGradeView.as_view(), name='add_grade'),
    path('teacher/attendance/<int:schedule_id>/', AttendanceView.as_view(),
         name='attendance'),

    # Студенты
    path('student/login/', StudentLoginView.as_view(), name='student_login'),
    path('student/logout/', StudentLogoutView.as_view(),
         name='student_logout'),
    path('student/dashboard/', StudentDashboardView.as_view(),
         name='student_dashboard'),
    path('student/schedule/', StudentScheduleView.as_view(),
         name='student_schedule'),
    path('student/grades/', StudentGradesView.as_view(),
         name='student_grades'),
    path('student/attendance/', StudentAttendanceView.as_view(),
         name='student_attendance'),
    path('student/settings/', StudentSettingsView.as_view(),
         name='student_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
