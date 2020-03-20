from rest_framework.views import APIView

from django.views import View
from django.shortcuts import HttpResponse

from .serializers import URLSerializer
from .models import URL

class Index(View):
    def get(self, request):
        return HttpResponse('Hello')


class Shortener(APIView):
    def post(self, request):
        pass
    
    def _fetch_title(self, original_url):
        pass


class Redirect(APIView):
    def get_url(self, key):
        pass

    def get(self, request, key):
        pass


class TopHundred(APIView):
    def get(self, request):
        pass