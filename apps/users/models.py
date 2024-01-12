from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя Студента'
    )
    direction = models.CharField(
        max_length = 255,
        verbose_name = 'Напрвление'
    )
    month = models.CharField(
        max_length = 255,
        verbose_name = 'Месяц обучения'
    )
    geek_coins = models.CharField(
        max_length = 255,
        verbose_name = 'Кол-во Coin '
    )

    def __str__(self):
        return f"{self.name}, {self.direction}" 
    
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


    