from django.db import models

from apps.users.models import User
# Create your models here.

class Transactions(models.Model):
    from_user = models.ForeignKey(User,
    on_delete=models.CASCADE, 
    related_name = 'from_user',
    verbose_name = 'От пользователя'
    )
    to_user = models.ForeignKey(User, 
    on_delete=models.CASCADE,
    related_name = 'to_user',
    verbose_name = 'К пользователя'
    )
    is_complated = models.BooleanField(
        default = False,
        verbose_name = 'Статус'
    )
    create_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата созадния'
    )
    amount = models.SmallIntegerField(
        verbose_name = "Кол-во Coins"
    )

    # def __str__(self):
    #     return self.from_user
    
    class Meta:
        verbose_name = 'Транзакия'
        verbose_name_plural = "Транзакции"




   
        


