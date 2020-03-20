from django.db import models


class VisitsManager(models.Manager):
    def get_queryset(self):
        pass


class URL(models.Model):
    pass
