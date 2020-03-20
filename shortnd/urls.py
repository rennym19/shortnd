from django.contrib import admin
from django.urls import path, include

from .shorturls import urls as short_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(short_urls, namespace='shortnd'))
]
