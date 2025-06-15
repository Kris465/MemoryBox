
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL Изображения")
    stock = models.IntegerField(default=0, verbose_name="Количество на складе")

    class Meta:
        verbose_name = "Продукт магазина"
        verbose_name_plural = "Продукты магазина"

    def __str__(self):
        return self.name
