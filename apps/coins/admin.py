from django.contrib import admin

from apps.coins.models import Coin
# Register your models here.

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('from_username', 'to_username', 'amount')
    list_filter = ( 'from_username', 'to_username', 'amount')

    