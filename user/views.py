import random
import string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSignupSerializer
from utils.redis import Redis


# Create your views here.