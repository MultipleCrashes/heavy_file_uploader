from django.shortcuts import render
from django.db.generic import View
# Create your views here
from .models import *

class Videos(View):
    def __init__(self):
        pass
   
    def dispatch(self, request, *args, **kwargs):
        pass 
 
    def post(self, request):
        request_data = request.POST
        try:
            Videos.objects.filter().values('video_url')
        except Except, e:
            pass          
        pass
   
    def get(self, request):
        pass
