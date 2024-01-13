from django.urls import path

from apps.transactions.views import TransactionsAPI, TransactionsAPICreate, TransactionsAPIRetrieve, TransactionsAPIUpdate, TransactionsAPIDestroy

urlpatterns = [
    path('', TransactionsAPI.as_view(), name='api_transactions'),
    path('create/', TransactionsAPICreate.as_view(), name='api_transactions_create'),
    path('<int:pk>/', TransactionsAPIRetrieve.as_view(), name='api_transactions_retrieve'),
    path('update/<int:pk>/', TransactionsAPIUpdate.as_view(), name='api_transactions_update'),
    path('destroy/<int:pk>/', TransactionsAPIDestroy.as_view(), name='api_transactions_destroy'),


]