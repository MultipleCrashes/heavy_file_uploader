from __future__ import unicode_literals

from django.db import models
# Create your models here.

class AnalyticsSource(models.Model):
    file_url = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
