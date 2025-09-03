
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    category = models.CharField(max_length=100, default='Общее', verbose_name="Категория")
    image = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL Изображения")
    content = models.TextField(verbose_name="Полное содержание")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Пост блога"
        verbose_name_plural = "Посты блога"

    def __str__(self):
        return self.title
