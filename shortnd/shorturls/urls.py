from django.urls import path, include
from .views import Index, Shortener, Redirect, TopHundred

app_name = 'shortnd'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<key>/', Redirect.as_view(), name='redirect'),
    path('shorten/', Shortener.as_view(), name='shorten'),
    path('top_hundred/', TopHundred.as_view(), name='top_hundred')
]
