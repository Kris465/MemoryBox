from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


from .forms import StudentForm, TeacherForm, SubjectForm, StatementForm
from .models import Student, Teacher, Subject, Statement




class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)
    

def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, template_name: 'index.html')



def students(request):
    students = Student.object.all()
    context = {
        'students': students,
    }
    return render(request, template_name 'student_list.html', context)


def display_students(request):
    students = Student.object.all()
    context = {
        'students': students,
        'header': 'Список студентов'
    }

    return render(request, template_name 'student_list.html', context)

def add_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentFrom()
        context = {
            'form': form,
            'header': 'Добавить студента'
        }
            
        return render(request, template_name 'add=_student.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
        'header': 'Детальная информация о студенте'
    }

    return render(request, template_name 'student_detail.html', context)


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method =='POST':
        form = StudentForm(request.POST, request.FILES, isinstance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(isinstance=student)
        context = {
            'form': form,
            'header': 'редактировать студента',
    }

    return render(request, template_name:'edit_student.html', context)



def delete_student (request, pk):
    students = get_object_or_404(Student, pk=pk)
    students.delete()
    return.redirect("student_list")


def print_students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, template_name: 'student_list.html', context)



def teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, template_name: 'teacher_list.html', context)


def display_teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'header': 'Список преподавателей'
    }
    return render(request, template_name: 'teacher_list.html', context)


def add_teacher(request):
    if request.method =='POST':
        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
        context = {
            'form': form,
            'header': 'Добавить преподавателя',
        }
        return render(request, template_name: 'add_teacher.html', context)



def subjects(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, template_name: 'subjects_list.html', context)


def display_subjects(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects': subjects,
        'header': 'spisok predmetov'
    }
    return render(request, template_name: 'subjects_list.html', context)


def add_subjects(request):
    if request.method =='POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
        context = {
            'form': form,
            'header': 'Добавить предмет',
        }
        return render(request, template_name: 'add_subjects.html', context)
    


def statements(request):
    statements = Statement.objects.all()
    context = {
        'statements': statements,
    }
    return render(request, template_name: 'statements_list.html', context)


def display_statements(request):
    statements = Statements.objects.all()
    context = {
        'statements': statements,
        'header': 'Ведомость успеваемости и посещаемости' 

    }
    return render(request, template_name: 'statements_list.html', context)


def add_statement(request):
    if request.method =='POST':
        form = StatementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('statement_list')
    else:
        form = TeacherForm()
        context = {
            'form': form,
            'header': 'Добавить успеваемость',
        }
        return render(request, template_name: 'add_statement.html', context)


def edit_statement(request, pk):
    statement = get_object_or_404(Statement, pk=pk)

    if request.method =='POST':
        form = StatementForm(request.POST, isinstance=statement)
        if form.is_valid():
            form.save()
            return redirect('statement_list')
        
    else:
        form = StatementForm(instance=statement)
        context = {
            'form': form,
            'header': 'Редактировать успеваемость',
        }
        return render(request, template_name: 'edit_statement.html', context)


def statement_detail(request, pk):
    statement = get_object_or_404(statement, pk=pk)
    context = {
        'statement': statement,
    }
    return render(request, template_name: 'statement_detail.html', context)


def delete_statements(request, pk):
    statements = get_object_or_404(Statement, pk=pk)
    statements.delete()
    return redirect("statement_list")


def search_statements(request):
    attendance = request.GET.get('attendance')
    if attendance:
        statements = Statement.objects.filter(attendance__icontains=attendance)
        header = f"Search results for '{attendance}'"
    else:
        statements = Statement.objects.all()
        header = "All Statements"
    context = {
        'statements': statements,
        'header': 'header' 

    }
    return render(request, template_name: 'statements_list.html', context)


def print_statement(request):
    statements = Statement.object.all()
    context = {
        'statements': statements,
    }
    return render(request, template_name: 'statement_detail.html', context)
