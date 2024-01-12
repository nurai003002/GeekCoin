from django.contrib import admin
from apps.users.models import Users

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'month', 'geek_coins')
    list_filter = ('name', 'direction', 'month', 'geek_coins')