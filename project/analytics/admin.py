from django.contrib import admin
from .models import *
# Register your models here.

class AnalyticsAdmin(admin.ModelAdmin):
    pass 

admin.site.register(AnalyticsSource,AnalyticsAdmin)
