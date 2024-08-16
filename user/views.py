import jwt
import requests
from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from config.settings.base import JWT_SECRET, KAKAO_API_KEY, KAKAO_REDIRECT_URI, KAKAO_CLIENT_SECRET
from user.models import User
from user.serializers import UserSignupSerializer


# Create your views here.
class UserSignupView(APIView):
    @transaction.atomic
    def post(self, request: object) -> Response:
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TokenVerifyView(APIView):
    def get(self, request: object) -> Response:
        header = request.headers.get('Authorization')

        if not header:
            return Response({'isValidToken': False, 'message': 'Empty token'}, status=status.HTTP_401_UNAUTHORIZED)

        token_type, token = header.split(' ')
        if token_type.lower() != 'bearer':
            return Response({'isValidToken': False}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return Response({'isValidToken': True})
        except Exception as e:
            return Response({'isValidToken': False, 'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class KakaoSignInView(APIView):
    def get(self, request: object) -> Response:
        data = {
            "redirect_url": f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_API_KEY}&redirect_uri={KAKAO_REDIRECT_URI}"
        }
        return Response(data, status=status.HTTP_302_FOUND)


class KakaoSignInCallbackView(APIView):
    @transaction.atomic
    def get(self, request: object) -> Response:

        """
            Get access token
        """
        code = request.GET.get('code')
        token_url = "https://kauth.kakao.com/oauth/token"
        token_data = {
            "grant_type": "authorization_code",
            "client_id": KAKAO_API_KEY,
            "redirect_uri": KAKAO_REDIRECT_URI,
            "code": code,
            "client_secret": KAKAO_CLIENT_SECRET
        }
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code != 200:
            return Response(r.json(), status=r.status_code)
        """
            Get user info
        """
        user_info = requests.get(
            url="https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {r.json().get('access_token')}"}
        )
        if user_info.status_code != 200:
            return Response(user_info.json(), status=user_info.status_code)

        email = user_info.json()["kakao_account"]["email"]
        user = User.objects.filter(email=email).first()
        if not user:
            """
            Todo
            create -> create_user
            (kakao oauth2)
            """
            user = User.objects.create(email=email)

        token = TokenObtainPairSerializer.get_token(user)

        access = str(token.access_token)
        refresh = str(token)

        data = {
            "access": access,
            "refresh": refresh
        }

        return Response(data, status=status.HTTP_200_OK)
