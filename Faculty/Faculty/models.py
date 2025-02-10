from django.db import models

# Create your models here.

class Student(models.Model):
    objects = None
    surname = models.CharField(max_length=100, help_text="vvedite phamiliy studenta" verbose_name="phamilia")
    name = models.CharField(max_length=100, help_text="vvedite imy studenta" verbose_name="imy")
    date_of_birth = models.DateField(help_text="vvedite data born" verbose_name="born",
                                     null=True, blank=True)
    group = models.CharField(max_length=100, help_text="vvedite # group" verbose_name="group")
    photo = models.ImageField(upload_to='images',
                            help_text="vvedite photo",
                            verbose_name="photo teacher",
                            null=True, blank=True)
    def __str__(self):
        return f'phamilia: {self.surname},imy: {self.name}'
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


    class Teacher(models.Model):
        objects = None
        surname = models.CharField(max_length=100, help_text="vvedite phamiliy" verbose_name="phamilia")
        name = models.CharField(max_length=100, help_text="vvedite imy studenta" verbose_name="imy")
        photo = models.ImageField(upload_to='images',
                            help_text="vvedite photo",
                            verbose_name="photo преподавателя",
                            null=True, blank=True)
        def __str__(self):
           return f'phamilia: {self.surname},imy: {self.name}'
    
        class Meta:
            verbose_name = 'преподаватель'
            verbose_name_plural = 'преподаватели'

    class Subject(models.Model):
        objects = None
        surname = models.CharField(max_length=100, help_text="vvedite nazvanie predmeta" verbose_name="predmeta")
        name = models.CharField(max_length=100, help_text="vvedite imy studenta" verbose_name="imy")
        teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, verbose_name="PREPODAVATEL")
        def __str__(self):
           return f'NAUM PREDMETA: {self.name} - PREPODAVATEL : {self.teacher}'
        
        class Meta:
            verbose_name = 'преподаватель'
            verbose_name_plural = 'преподаватель'


    class Statement(models.Model):
         objects = None
         Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='statements' verbose_name='студент')
         subject = models.ForeignKey(subject, on_delete=models.CASCADE, verbose_name='predmet')
         ATTENDANCE_CHOICES= [
            ('VYSOK','VYSOK'),
            ('CRED', 'CRED'),
            ('NIZK','NIZK'),
         ]
    attendance = models.CharField(max_length=50, choices=ATTENDANCE_CHOICES, verbose_name='POSEHAEMOST')
    grade_choices= [
            ('VYSOK','VYSOK'),
            ('CRED', 'CRED'),
            ('NIZK','NIZK'),
    ]
    grade = models.CharField(max_length=50, choices=grade_choices, verbose_name='USPEVAEMOST')
    ESTIMATION_CHOISES = [
            ('VYSOK','VYSOK'),
            ('CRED', 'CRED'),
            ('NIZK','NIZK'),
    ]
    estimation = models.CharField(max_length=50, choices=ESTIMATION_CHOISES, help_text='vystavit ozenky' verbose_name='ozenka')
    date__of_rating = models.DateField(verbose_name='Data vystavlenia', null=True, blank=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='prepodavatel')

    def __str__(self):
           return f'{self.student} {self.estimation}'

    class Meta:
        verbose_name = 'Ведомости'
        verbose_name_plural = 'Ведомости'