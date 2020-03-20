from django.db import models
from django.contrib.sites.models import Site


class VisitsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-visit_count')[:100]


class URL(models.Model):
    original_url = models.TextField(max_length=2048, unique=True)
    key = models.CharField(max_length=7, null=True)
    title = models.CharField(max_length=255, null=True)
    visit_count = models.IntegerField(null=True, default=0)

    objects = models.Manager()
    top_hundred = VisitsManager()

    @property
    def short_url(self):
        domain = Site.objects.get_current().domain
        return 'http://{0}/{1}/'.format(domain, self.key)
