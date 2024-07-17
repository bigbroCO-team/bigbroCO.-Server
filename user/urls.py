from django.urls import path
from .views import UserSignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    SendVerifyEmailView,
    VerifyEmailView,
    ResetPasswordView
)


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('signup', UserSignupView.as_view(), name='signup'),
    path('refresh', TokenRefreshView.as_view()),
    path('verify', TokenVerifyView.as_view()),

    path('code', SendVerifyEmailView.as_view()),
    path('verify', VerifyEmailView.as_view()),
    path('reset', ResetPasswordView.as_view()),
]
