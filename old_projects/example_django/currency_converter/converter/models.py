from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.char_code} ({self.name}): {self.rate}"
