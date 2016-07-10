from django.contrib import admin

# Register your models here.

from .models import *

class VideosAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Videos, VideosAdmin)
