from django.urls import path

from apps.coins.views import CoinAPI, CoinCreate

urlpatterns = [
    path('', CoinAPI.as_view(), name='api_coins'),
    path('create/', CoinCreate.as_view(), name='api_coins_create' )
]