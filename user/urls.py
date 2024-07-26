from django.urls import path
from .views import UserSignupView, TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('/login', TokenObtainPairView.as_view(), name='login'),
    path('/signup', UserSignupView.as_view(), name='signup'),
    path('/refresh', TokenRefreshView.as_view()),
    path('/verify', TokenVerifyView.as_view(), name='verify'),
]
