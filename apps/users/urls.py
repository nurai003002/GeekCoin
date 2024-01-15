from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserAPIViewsSet

router = DefaultRouter()

router.register('user', UserAPIViewsSet, 'api_user')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_user_refresh'),
    
]