from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from src.app.client.product.models import Product


class ProductTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            category='CBWAS',
            name='CBWAS',
            description='CBWAS',
            price=10000,
            discount=0
        )

    def test_get_product_list(self):
        path = reverse('product-list')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_get_product_detail(self):
        path = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.get(path)
        assert response.status_code == 200