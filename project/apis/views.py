from django.shortcuts import render
from .models import *
from django.views.generic import View 
# Create your views here.

class ApiStructure(View):
    def __init__(self):
        pass 

    def dispatch(self, request):
        return super(ApiStructure, self).dispatch(*args, **kwars) 

    def post(self, request):
        req_data = request.POST
        pass 

    def get(self, request):
        req_data = request.GET 
        pass 
