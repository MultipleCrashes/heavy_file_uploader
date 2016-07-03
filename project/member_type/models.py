from __future__ import unicode_literals

from django.db import models

# Create your models here.



class MemberType(models.Model):
    member_id = models.CharField(max_length=255,primary_key=True)
    member_type = models.CharField(max_length=255)
    membership_fee = models.IntegerField()

