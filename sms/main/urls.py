from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views.admin_view import (
    AdminLoginView,
    AdminLogoutView,
    AdminDashboardView,
    StudentManagementView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    AboutPageView,
    ContactPageView
)
from main.views.students_view import (
    StudentLoginView,
    StudentLogoutView,
    StudentDashboardView,
    StudentScheduleView,
    StudentGradesView,
    StudentAttendanceView,
    StudentSettingsView
)
from main.views.teachers_view import (
    TeacherDashboardView,
    TeacherScheduleView,
    GradeBookView,
    AddGradeView,
    AttendanceView,
    TeacherLoginView
)
from main.views.common_views import (
    HomeView,
    AboutView,
    ContactView
)

urlpatterns = [
    # Основные страницы
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),

    # Админ-панель
    path('admin/login/', AdminLoginView.as_view(),
         name='admin_login'),
    path('admin/logout/', AdminLogoutView.as_view(),
         name='admin_logout'),
    path('admin/dashboard/', AdminDashboardView.as_view(),
         name='admin_dashboard'),
    path('admin/students/', StudentManagementView.as_view(),
         name='manage_students'),
    path('admin/students/add/', StudentCreateView.as_view(),
         name='add_student'),
    path('admin/students/<int:id>/update/', StudentUpdateView.as_view(),
         name='update_student'),
    path('admin/students/<int:id>/delete/', StudentDeleteView.as_view(),
         name='delete_student'),
    path('admin/about/', AboutPageView.as_view(), name='admin_about'),
    path('admin/contact/', ContactPageView.as_view(), name='admin_contact'),

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

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
