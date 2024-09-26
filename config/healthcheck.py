from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    def get(self, request: object) -> Response:
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
