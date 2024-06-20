from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RatingSerializer, ReviewSerializer
from .models import Rating, Review
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class RatingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ReviewView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]