from django.urls import path

from account.views import TokenVerifyView
from account.KakaoView import KakaoSignInView, KakaoSignInCallbackView

urlpatterns = [
    path('verify/', TokenVerifyView.as_view(), name='verify'),

    path('kakao/', KakaoSignInView.as_view()),
    path('kakao/callback/', KakaoSignInCallbackView.as_view())
]