from drf_spectacular.utils import extend_schema_view, extend_schema

from account.KakaoService import KakaoService
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bigbro.settings import KAKAO_REDIRECT_URI, KAKAO_API_KEY

@extend_schema_view(
    get=extend_schema(
        summary='Kakao Signin API',
        description='Kakao OAuth login API 입니다. 로그인 성공 시 access, refresh 토큰이 발급됩니다.',
    )
)
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
