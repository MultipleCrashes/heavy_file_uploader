from django.contrib import admin
from .models import *
# Register your models here.

class PayeeDetailsAdmin(admin.ModelAdmin):
    pass 


admin.site.register(PayeeDetails,PayeeDetailsAdmin)
