from django.db import models


from apps.users.models import User
# Create your models here.
class Coin(models.Model):
    to_username = models.CharField(
        max_length = 255,
        verbose_name = 'Получатель'
    )
    from_username = models.CharField(
        max_length = 255,
        verbose_name = 'Отправитель'
    )
    amount = models.SmallIntegerField(
        default = 0, verbose_name = 'Кол-во coins'
    )

    def __str__(self):
        return self.to_username
    
    class Meta:
        verbose_name = 'Коин'
        verbose_name_plural = 'Коины'
