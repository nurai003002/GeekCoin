from django.urls import path

from apps.users.views import UsersAPI, UsersAPICreate, UsersAPIRetrieve, UsersAPIUpdate, UsersAPIDestroy

urlpatterns = [
    path('', UsersAPI.as_view(), name='api_users'),
    path('create/', UsersAPICreate.as_view(), name='api_users_create'),
    path('<int:pk>/', UsersAPIRetrieve.as_view(), name='api_users_retrieve'),
    path('update/<int:pk>/', UsersAPIUpdate.as_view(), name='api_users_update'),
    path('destroy/<int:pk>/', UsersAPIDestroy.as_view(), name='api_users_destroy'),


]