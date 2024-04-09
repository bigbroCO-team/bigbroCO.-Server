from typing import Any
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JwtHandler:
    @classmethod
    def setToken(cls, user: Any) -> Response:
        r = Response({}, status=status.HTTP_200_OK)
        token = TokenObtainPairSerializer.get_token(user)
        r.set_cookie('access_token', str(token.access_token), max_age=60, httponly=True)
        r.set_cookie('refresh_token', str(token), max_age=604800, httponly=True)  # 7day
        return r

    @classmethod
    def deleteToken(cls):
        r = Response({}, status=status.HTTP_200_OK)
        r.delete_cookie("access_token")
        r.delete_cookie("refresh_token")
        return r
