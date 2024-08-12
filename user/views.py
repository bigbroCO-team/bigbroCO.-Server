import jwt
import requests
from django.db import transaction
from django.shortcuts import redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from config.settings.base import JWT_SECRET
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
    def post(self, request: object) -> Response:
        try:
            access_token = request.data.get('token')
            user_info = requests.get(
                url="https://kapi.kakao.com/v2/user/me",
                headers={"Authorization": f"Bearer {access_token}"}
            ).json()
            email = user_info["kakao_account"]["email"]
            user = User.objects.filter(email=email).first()
            if not user:
                user = User.objects.create(email=email)

            token = TokenObtainPairSerializer.get_token(user)

            access = str(token.access_token)
            refresh = str(token)

            data = {
                "access": access,
                "refresh": refresh
            }

            return Response(data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "KeyError"}, status=status.HTTP_401_UNAUTHORIZED)
