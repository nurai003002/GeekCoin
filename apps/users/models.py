from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефон номера'
    )
    age = models.PositiveIntegerField(
        verbose_name = 'Возраст струдента',
        blank = True, null= True
    )
    direction = models.CharField(
        max_length = 255,
        verbose_name = 'Напрваление'
    )
    balance = models.IntegerField(
        verbose_name = 'Баланс',
        default = 4,
        blank = True, null=True
    )
    wallet_address = models.CharField(
        max_length = 16,
        verbose_name = 'Кошелк',
        blank = True, null=True,
        unique = True
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


