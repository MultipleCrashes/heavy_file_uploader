from django.contrib import admin
from .models import *
# Register your models here.

class MemberTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(MemberType,MemberTypeAdmin)
