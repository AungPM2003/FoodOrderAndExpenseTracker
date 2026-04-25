from django.shortcuts import render
from django.http import request,HttpResponse
from .models import Food
# Create your views here.
def index(reqeust):
    foods = Food.objects.all()
    print(foods)
    context = {"foods":foods}
    return render(request,"index.html",context)
