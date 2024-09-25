from django.urls import path

from src.app.user.views import TokenVerifyView
from src.app.user.KakaoView import KakaoSignInView, KakaoSignInCallbackView

urlpatterns = [
    path('/verify', TokenVerifyView.as_view(), name='verify'),

    path('/kakao', KakaoSignInView.as_view()),
    path('/kakao/callback', KakaoSignInCallbackView.as_view())
]