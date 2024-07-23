import jwt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings.base import JWT_SECRET
from user.serializers import UserSignupSerializer


# Create your views here.
class UserSignupView(APIView):
    def post(self, request: object) -> Response:
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TokenVerifyView(APIView):
    def post(self, request: object) -> Response:
        token = request.data.get('token')

        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return Response({'isValidToken': True})
        except:
            return Response({'isValidToken': False}, status=status.HTTP_401_UNAUTHORIZED)
