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


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                              related_name='student_profile')
    father_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    mother_name = models.CharField(max_length=100, blank=True, verbose_name='Мать')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    course = models.ForeignKey('Course', on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name='Курс')
    stu_id = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        verbose_name='ID студента',
        validators=[MinLengthValidator(5)]
    )


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='teacher_profile')
    qualification = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Course(models.Model):
    COURSE_TYPES = [
        ('lecture', 'Лекция'),
        ('seminar', 'Семинар'),
        ('lab', 'Лабораторная работа'),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    credits = models.PositiveSmallIntegerField(default=3)
    course_type = models.CharField(
        max_length=10,
        choices=COURSE_TYPES,
        default='lecture'
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True)

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

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    numeric_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    letter_grade = models.CharField(
        max_length=1,
        choices=GRADE_CHOICES,
        blank=True
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True)

    class Meta:
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
    about = models.TextField()

    def __str__(self):
        return "About Page Content"


class ContactPage(models.Model):
    address = models.TextField()
    contact_num = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Contact Information"


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    start_time = models.DateTimeField(verbose_name='Начало')
    end_time = models.DateTimeField(verbose_name='Окончание')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,
                                null=True, blank=True, verbose_name='Преподаватель')

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
        unique_together = ['student', 'schedule']
        verbose_name = 'Посещаемость'
        verbose_name_plural = 'Посещаемость'

    @property
    def date(self):
        return self.schedule.start_time.date()
