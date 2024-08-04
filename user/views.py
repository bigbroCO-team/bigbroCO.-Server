import jwt
from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings.base import JWT_SECRET
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
            return Response({'isValidToken': False, 'message': e}, status=status.HTTP_401_UNAUTHORIZED)
