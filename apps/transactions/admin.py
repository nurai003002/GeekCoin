from django.contrib import admin

from apps.transactions.models import Transactions
# Register your models here.

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user_get', 'sender', 'coin_amount', 'month')
    list_filter = ('user_get', 'sender', 'coin_amount', 'month')
