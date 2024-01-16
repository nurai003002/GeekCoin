from django.contrib import admin

from apps.transactions.models import Transactions
# Register your models here.

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('from_user' ,'to_user', 'is_complated', 'create_at','amount')
    list_filter = ('from_user' ,'to_user', 'is_complated', 'create_at','amount')
