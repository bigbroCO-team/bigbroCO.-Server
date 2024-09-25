import jwt
from django.db import transaction
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from config.settings.base import SECRET_KEY


@extend_schema_view(
    get=extend_schema(
        summary='Token verify view API',
        description='Access token 검증 API 입니다.',
        parameters=[
            OpenApiParameter(
                name='Authorization',
                required=True,
                location=OpenApiParameter.HEADER
            )
        ]
    ))
class TokenVerifyView(APIView):
    @transaction.atomic
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