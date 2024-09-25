from src.app.user.KakaoService import KakaoService
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from config.settings.base import KAKAO_REDIRECT_URI, KAKAO_API_KEY


class KakaoSignInView(APIView):
    def get(self, request: object) -> Response:
        headers = {"Location": f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_API_KEY}&redirect_uri={KAKAO_REDIRECT_URI}"}
        return Response(headers=headers, status=status.HTTP_302_FOUND)


class KakaoSignInCallbackView(APIView):
    @transaction.atomic
    def get(self, request: object) -> Response:
        code = request.GET.get('code')
        access_code = KakaoService.get_access_token(code)
        email = KakaoService.get_user_email(access_code)
        return KakaoService.get_token(email)
