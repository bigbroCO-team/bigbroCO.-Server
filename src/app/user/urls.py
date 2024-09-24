from django.urls import path

from .views import KakaoSignInView, KakaoSignInCallbackView, TokenVerifyView


urlpatterns = [
    path('/verify', TokenVerifyView.as_view(), name='verify'),

    path('/kakao', KakaoSignInView.as_view()),
    path('/kakao/callback', KakaoSignInCallbackView.as_view())
]
