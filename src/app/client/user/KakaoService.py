import requests
from config.utils.exception.CustomException import CustomException
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from src.app.client.user.models import User
from datetime import timedelta
from config.settings.base import (
    KAKAO_REDIRECT_URI,
    KAKAO_API_KEY,
    KAKAO_CLIENT_SECRET,
    CLIENT_REDIRECT_URL
)


class KakaoService:

    @staticmethod
    def get_access_token(code):
        response = requests.post(
            url="https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": KAKAO_API_KEY,
                "redirect_uri": KAKAO_REDIRECT_URI,
                "code": code,
                "client_secret": KAKAO_CLIENT_SECRET
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )

        if response.status_code != 200:
            raise CustomException.KakaoOAuthCodeIsNotValid
        return response.json().get('access_token')

    @staticmethod
    def get_user_email(access_token):
        response = requests.get(
            url="https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        if response.status_code != 200:
            raise CustomException.KakaoOAuthAccessTokenIsNotValid
        return response.json().get('kakao_account').get('email')

    @staticmethod
    def get_token(email):
        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(email=email)

        token = TokenObtainPairSerializer.get_token(user)
        r = Response(
            headers={
                'Location': CLIENT_REDIRECT_URL,
            },
            status=status.HTTP_302_FOUND,
        )

        r.set_cookie('access', str(token.access_token), expires=timedelta(minutes=1))
        r.set_cookie('refresh', str(token), expires=timedelta(minutes=1))
        return r
