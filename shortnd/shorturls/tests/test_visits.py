from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..models import URL
from ..serializers import URLSerializer
from ..key_generator import gen_key


class VisitsTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.visit_view_name = 'shortnd:redirect'
        self.top_hundred_url = reverse('shortnd:top_hundred')

        url = URL(original_url='https://www.apple.com', title='Apple', key=gen_key(url_id=1), visit_count=50)
        url.save()
        self.url = url

        second_url = URL(original_url='https://www.android.com', title='Android', key=gen_key(url_id=2), visit_count=80)
        second_url.save()
        self.second_url = second_url

    def test_visit_count_increments(self):
        response = self.client.get(reverse(self.visit_view_name, kwargs={'key': self.url.key}))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        url = URL.objects.get(original_url='https://www.apple.com')
        self.assertEqual(url.visit_count, 51)
        
    def test_top_hundred(self):
        response = self.client.get(self.top_hundred_url)
        serialized_data = URLSerializer(response.data['results'], many=True).data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(serialized_data[0]['id'], self.second_url.pk)
