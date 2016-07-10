from django.shortcuts import render
from django.views.generic import View
# Create your views here
from .models import *
from django.http import HttpResponse 
import json 

class VideosView(View):
    def __init__(self):
        pass
   
    #def dispatch(self, request, *args, **kwargs):
    #    pass 
 
    def post(self, request):
        request_data = request.POST
        print request_data
        video_url = []
        response = {}
        try:
            response = Videos.objects.all().values('url')[0]
            print response
        except Exception, e:
            print "Exception found while getting video url",str(e)
            pass          
        return HttpResponse(json.dumps(
                    response),content_type = 'application/json')
        
 
    def get(self, request):
        pass
