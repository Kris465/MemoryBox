from django.urls import path
from . import views
from .views import MainGradeView, main_grade

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.schedule_list, name='schedule_list'),
    path('about/', views.about, name="about"),
    path('search/', views.search, name='search'),
    path('add-grade/', views.add_grade, name='add_grade'),
    path('grades/', views.grades_list, name='grades_list'),
    path('grades/', MainGradeView.as_view(), name='main_grade'),
    path('grades/', main_grade, name='main_grade'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('list/', views.attendance_list, name='attendance_list'),
    path('contact/', views.contact, name="contact"),
    path('attendance/', views.attendance_form, name='attendance_form'),
    path('admin_panel/dashboard', views.adminPanel, name="admin_panel"),
    path('admin_panel/login/', views.adminLogin, name="admin_login"),

    path('ladmin_pane/logout/', views.adminLogout, name="admin_logout"),
    path('student/login/', views.studentLogin, name="student_login"),
    path('admin_panel/add_student/', views.addStudent, name="add_student"),
    path('admin_panel/about/', views.adminAbout, name="admin_about"),
    path('admin_panel/update_about/<str:id>/',
         views.updateAbout,
         name="update_about"),

    path('admin_panel/contact/', views.adminContact, name="admin_contact"),
    path('admin_panel/update_contact/<str:id>/', views.updateContact, name="update_contact"),
    path('admin_panel/manage_students/', views.manageStudent, name="manage_students"),
    path('admin_panel/update_student/<str:id>/', views.updateStudent, name="update_student"),
    path('admin_panel/delete_student/<str:id>/', views.deleteStudent, name="delete_student"),
    path('admin_panel/add_notice/', views.addNotice, name="add_notice"),

    path('admin_panel/manage_notices/', views.manageNotices, name="manage_notices"),
    path('admin_panel/delete_notice/<str:id>/', views.deleteNotice, name="delete_notice"),
    path('admin_panel/update_notice/<str:id>/', views.updateNotice, name="update_notice"),

    path('admin_panel/add_teacher/', views.addTeacher, name="add_teacher"),
    path('admin_panel/manage_teacher/', views.manageTeachers, name="manage_teachers"),
    path('admin_panel/delete_teacher/<str:id>/', views.deleteTeacher, name="delete_teacher"),

    path('student/dashboard/',
         views.studentDashboard,
         name="student_dashboard"),
    path('student/logout/', views.studentLogout, name="student_logout"),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
    path('student/update_teacher/<str:id>/', views.updateFaculty, name="update_teacher"),
    path('student/view_notices/', views.viewNotices, name="view_notices"),
    path('student/student_settings/', views.studentSettings, name="student_settings")
]
