from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product
from utils.utils import testcode_admin_authentication


# Create your tests here.
class ProductTestCase(APITestCase):

    def setUp(self):
        testcode_admin_authentication(self)

    def test_upload_product(self):
        url = reverse('admin-product')
        data = {
            "name": "test",
            "description": "test?",
            "open_stock": 0,
            "price": 30000,
            "discount": 0,
            "category": "BIGBRO",
            "options": [
                {
                    "name": "test",
                    "stock": 1
                }
            ],
            "images": [
                {
                    "url": "a.png"
                }
            ]
        }

        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
