import random
import string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSignupSerializer
from utils.redis import Redis


# Create your views here.
class UserSignupView(APIView):
    def post(self, request: object) -> Response:
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
