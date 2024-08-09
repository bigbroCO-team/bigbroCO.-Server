# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from order.serializers import ProductItemSerializer


class CreateOrderListView(APIView):
    pass
