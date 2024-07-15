from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class UploadAddressTestCode(APITestCase):
    def test_upload_address(self):
        url = reverse('address')
        data = {
                "tag": "test",
                "zipcode": 12345,
                "address": "test",
                "detail": "test",
                "request": "test"
        }

        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
