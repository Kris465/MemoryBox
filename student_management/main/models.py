from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание")
    start_date = models.DateField(verbose_name="Начало курса")
    end_date = models.DateField(verbose_name="Окончание курса")
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Преподаватель",
        related_name='taught_courses'
    )

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='student_profile')
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    class Meta:
        verbose_name = 'Профиль студента'
        verbose_name_plural = 'Профили студентов'

    def __str__(self):
        return f"Студент: {self.user.username}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='teacher_profile')
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    class Meta:
        verbose_name = 'Профиль преподавателя'
        verbose_name_plural = 'Профили преподавателей'

    def __str__(self):
        return f"Преподаватель: {self.user.username}"


class Schedule(models.Model):
    DAYS_OF_WEEK = (
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='schedules')
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK,
                           verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    class Meta:
        ordering = ['day', 'start_time']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return f"{self.course.name} - {self.get_day_display()}"


class Grade(models.Model):
    GRADE_CHOICES = (
        (5, 'Отлично (A)'),
        (4, 'Хорошо (B)'),
        (3, 'Удовлетворительно (C)'),
        (2, 'Неудовлетворительно (D)'),
        (1, 'Провал (F)'),
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Студент"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Курс"
    )
    value = models.IntegerField(choices=GRADE_CHOICES, verbose_name="Оценка")
    date = models.DateField(auto_now_add=True, verbose_name="Дата оценки")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        unique_together = [['student', 'course']]

    def __str__(self):
        return f"{self.student.username} - {self.course.name}: {self.get_value_display()}"
