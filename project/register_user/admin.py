from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_per_page = 100
    search_field = ['first_name','last_name','country','state']
    
admin.site.register(User,UserAdmin)

