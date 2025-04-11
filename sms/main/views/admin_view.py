from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .mixins import AdminAuthMixin
from main.models import (
    Student, Teacher, Course,
    AboutPage, ContactPage, User
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminLoginView(View):
    template_name = 'admin/admin_login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('admin_dashboard')
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')

        messages.error(request, 'Неверные учетные данные')
        return render(request, self.template_name)


class AdminLogoutView(View):
    """Выход из системы администратора"""
    def get(self, request):
        if 'admin_authenticated' in request.session:
            del request.session['admin_authenticated']
        return redirect('admin_login')


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'admin/admin_panel.html'
    login_url = '/admin/login/'

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        context = {
            'students_count': Student.objects.count(),
            'teachers_count': Teacher.objects.count(),
            'courses_count': Course.objects.count()
        }
        return render(request, self.template_name, context)


class StudentManagementView(AdminAuthMixin, View):
    """Управление студентами"""
    template_name = 'admin/manage_students.html'

    def get(self, request):
        students = Student.objects.all().select_related('user')
        return render(request, self.template_name, {'students': students})


class StudentCreateView(AdminAuthMixin, View):
    """Добавление нового студента"""
    template_name = 'admin/new_student.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            user = User.objects.create(
                username=request.POST.get('stu_user_name'),
                email=request.POST.get('stu_email'),
                password=make_password(request.POST.get('stu_pwd')),
                role='student',
                phone=request.POST.get('contact_number')
            )
            Student.objects.create(
                user=user,
                father_name=request.POST.get('f_name'),
                mother_name=request.POST.get('m_name'),
                date_of_birth=request.POST.get('dob'),
                course=request.POST.get('course'),
                stu_id=request.POST.get('stu_id')
            )

            messages.success(request, 'Студент успешно добавлен')
            return redirect('manage_students')

        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
            return render(request, self.template_name)


class StudentUpdateView(AdminAuthMixin, View):
    """Редактирование студента"""
    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        try:
            student.user.email = request.POST.get('stu_email')
            student.user.phone = request.POST.get('contact_number')
            student.user.save()

            student.father_name = request.POST.get('f_name')
            student.mother_name = request.POST.get('m_name')
            student.date_of_birth = request.POST.get('dob')
            student.course = request.POST.get('course')
            student.stu_id = request.POST.get('stu_id')
            student.save()

            messages.success(request, 'Данные студента обновлены')
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')

        return redirect('manage_students')


class StudentDeleteView(AdminAuthMixin, View):
    """Удаление студента"""
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.user.delete()
        messages.success(request, 'Студент удален')
        return redirect('manage_students')


class AboutPageView(AdminAuthMixin, View):
    """Управление страницей 'О нас'"""
    template_name = 'admin/admin_about.html'

    def get(self, request):
        about = AboutPage.objects.first()
        if not about:
            about = AboutPage.objects.create(about="Текст по умолчанию")
        return render(request, self.template_name, {'about': about})

    def post(self, request):
        about = AboutPage.objects.first()
        about.about = request.POST.get('text', '')
        about.save()
        messages.success(request, 'Страница обновлена')
        return redirect('admin_about')


class ContactPageView(AdminAuthMixin, View):
    """Управление контактной информацией"""
    template_name = 'admin/admin_contact.html'

    def get(self, request):
        contact = ContactPage.objects.first()
        if not contact:
            contact = ContactPage.objects.create(
                address="Ваш адрес",
                email="your@email.com",
                contact_num="1234567890"
            )
        return render(request, self.template_name, {'contact': contact})

    def post(self, request):
        contact = ContactPage.objects.first()
        contact.address = request.POST.get('address', '')
        contact.email = request.POST.get('email', '')
        contact.contact_num = request.POST.get('contact', '')
        contact.save()
        messages.success(request, 'Контактная информация обновлена')
        return redirect('admin_contact')
