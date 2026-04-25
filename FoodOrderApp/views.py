from django.shortcuts import render
from django.http import request,HttpResponse

# Create your views here.
def index(reqeust):
    return HttpResponse("Hello I am index")
