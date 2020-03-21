from django.db import models
from .title_crawler import fetch_title 

class VisitsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-visit_count')[:100]


class URL(models.Model):
    original_url = models.TextField()
    key = models.CharField(max_length=7, null=True, unique=True)
    short_url = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=255, null=True)
    visit_count = models.IntegerField(null=True, default=0)

    objects = models.Manager()
    top_hundred = VisitsManager()

    def fetch_title_if_not_set(self):
        if self.title is None or self.title == '':
            fetch_title(self)
