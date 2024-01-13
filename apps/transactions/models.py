from django.db import models

# Create your models here.

class Transactions(models.Model):
    user_get = models.CharField(
        max_length = 255,
        verbose_name = 'Получатель'
    )
    sender = models.CharField(
        max_length = 255,
        verbose_name = 'Отправитель'
    )
    coin_amount = models.SmallIntegerField(
        verbose_name = 'Кол-во Coin'
    )
    month = models.CharField(
        max_length = 255,
        verbose_name = 'Месяц обучения'
    )
    homework = models.SmallIntegerField(
        verbose_name = 'За какой дз'
    )
    def __str__(self):
        return self.user_get
    
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
