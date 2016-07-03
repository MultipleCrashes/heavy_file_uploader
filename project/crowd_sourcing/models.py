from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PayeeDetails(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    payee_location = models.CharField(max_length=255)    
    payee_sex = models.CharField(max_length=255)
    payee_age = models.IntegerField()
    payee_country = models.CharField(max_length=255)
      
