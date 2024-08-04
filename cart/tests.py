from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product
from utils.utils import testcode_basic_authentication


# Create your tests here.
class UploadAddressTestCode(APITestCase):
    obj: Product.objects

    def setUp(self):
        testcode_basic_authentication(self)
        self.obj = Product.objects.create(
            name="test",
            description="test",
            open_stock=True,
        )

    def test_upload_cart(self):
        url = reverse('cart')
        data = {
            "product": self.obj.id,
            "count": 2,
            "option": 1
        }

        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
