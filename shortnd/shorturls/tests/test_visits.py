from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..models import URL
from ..key_generator import gen_key

class VisitsTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.top_hundred_url = reverse('shortnd:top_hundred')

        url = URL(original_url='https://www.apple.com', title='Apple', key=gen_key(url_id=1), visit_count=50)
        url.save()
        self.url = url

        second_url = URL(original_url='https://www.android.com', title='Android', key=gen_key(url_id=2), visit_count=80)
        second_url.save()
        self.second_url = second_url

    def test_visit_count_increments(self):
        response = self.client.get(self.url.short_url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.url.visit_count, 81)
        
    def test_top_hundred(self):
        response = self.client.get(self.top_hundred_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0].key, self.second_url.key)
        self.assertEqual(response.data[1].key, self.url.key)
