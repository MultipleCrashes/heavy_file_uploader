from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Videos(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return str(self.url)
