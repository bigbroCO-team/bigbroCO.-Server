import jwt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from config.settings.base import SECRET_KEY


# Create your views here.
class TokenVerifyView(APIView):
    def get(self, request: object) -> Response:
        header = request.headers.get('Authorization')

        if not header:
            return Response({'isValidToken': False, 'message': 'Empty token'}, status=status.HTTP_401_UNAUTHORIZED)

        token_type, token = header.split(' ')
        if token_type.lower() != 'bearer':
            return Response({'isValidToken': False}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return Response({'isValidToken': True})
        except Exception as e:
            return Response({'isValidToken': False, 'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)