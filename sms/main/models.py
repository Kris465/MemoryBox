from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator, MinLengthValidator)
from django.forms import ValidationError


class User(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('teacher', 'Преподаватель'),
        ('student', 'Студент'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='student',
        verbose_name='Роль'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон',
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='student_profile',
                                verbose_name='Пользователь')
    father_name = models.CharField(max_length=100, blank=True,
                                   verbose_name='Отчество')
    mother_name = models.CharField(max_length=100, blank=True,
                                   verbose_name='Мать')
    date_of_birth = models.DateField(null=True, blank=True,
                                     verbose_name='Дата рождения')
    course = models.ForeignKey('Course', on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name='Курс')
    stu_id = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        verbose_name='ID студента',
        validators=[MinLengthValidator(5)]
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.stu_id or 'нет ID'})"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='teacher_profile',
                                verbose_name='Пользователь')
    qualification = models.TextField(blank=True, verbose_name='Квалификация')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return self.user.get_full_name()


class Course(models.Model):
    COURSE_TYPES = [
        ('lecture', 'Лекция'),
        ('seminar', 'Семинар'),
        ('lab', 'Лабораторная работа'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    code = models.CharField(max_length=20, unique=True,
                            verbose_name='Код курса')
    description = models.TextField(blank=True, verbose_name='Описание')
    credits = models.PositiveSmallIntegerField(default=3,
                                               verbose_name='Кредиты')
    course_type = models.CharField(
        max_length=10,
        choices=COURSE_TYPES,
        default='lecture',
        verbose_name='Тип курса'
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Преподаватель')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['code']

    def __str__(self):
        return f"{self.code}: {self.name}"


class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'Отлично (90-100)'),
        ('B', 'Хорошо (80-89)'),
        ('C', 'Удовлетворительно (70-79)'),
        ('D', 'Неудовлетворительно (60-69)'),
        ('F', 'Не сдано (0-59)'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name='Курс')
    date = models.DateField(verbose_name='Дата оценки')
    numeric_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='Числовая оценка'
    )
    letter_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        blank=True,
        verbose_name='Буквенная оценка'
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Преподаватель')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['-date']
        unique_together = ['student', 'course', 'date']

    def __str__(self):
        return f"{self.student} - {self.course}: {self.letter_grade} ({self.numeric_score})"

    def save(self, *args, **kwargs):
        if not self.letter_grade:
            if self.numeric_score >= 90:
                self.letter_grade = 'A'
            elif self.numeric_score >= 80:
                self.letter_grade = 'B'
            elif self.numeric_score >= 70:
                self.letter_grade = 'C'
            elif self.numeric_score >= 60:
                self.letter_grade = 'D'
            else:
                self.letter_grade = 'F'
        super().save(*args, **kwargs)


class AboutPage(models.Model):
    about = models.TextField(verbose_name='Текст страницы')

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страницы "О нас"'

    def __str__(self):
        return "Содержание страницы 'О нас'"


class ContactPage(models.Model):
    address = models.TextField(verbose_name='Адрес')
    contact_num = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return "Контактная информация"


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    start_time = models.DateTimeField(verbose_name='Начало')
    end_time = models.DateTimeField(verbose_name='Окончание')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Преподаватель')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['start_time']

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Время окончания должно быть позже времени начала')

    def __str__(self):
        return f"{self.course.name} ({self.start_time:%d.%m.%Y %H:%M})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Присутствовал'),
        ('absent', 'Отсутствовал'),
        ('late', 'Опоздал'),
        ('excused', 'По уважительной причине'),
    ]

    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name='Студент'
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='Занятие'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='present',
        verbose_name='Статус'
    )
    notes = models.TextField(blank=True, verbose_name='Примечания')

    class Meta:
        verbose_name = 'Посещаемость'
        verbose_name_plural = 'Посещаемость'
        unique_together = ['student', 'schedule']
        ordering = ['schedule__start_time']

    @property
    def date(self):
        return self.schedule.start_time.date()

    def __str__(self):
        return f"{self.student} - {self.schedule}: {self.get_status_display()}"
