from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactPage(models.Model):
    address = models.TextField()
    contact_num = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.address


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default="Male")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.IntegerField(default=1234567)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    stu_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


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

    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
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

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} - {self.course}: {self.letter_grade}"

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


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.date} - {'Present' if self.
                                                     is_present else 'Absent'}"


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField()

    def __str__(self):
        return self.full_name
