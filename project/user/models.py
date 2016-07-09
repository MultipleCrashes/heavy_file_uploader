from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)  # data of birth 
    country = models.CharField(max_length=255) 
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
  

 
