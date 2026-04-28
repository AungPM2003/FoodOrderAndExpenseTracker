from django.shortcuts import render
from django.http import request,HttpResponse
from django.views.generic import ListView
from .models import Food
# Create your views here.
# def index(reqeust):
#     foods = Food.objects.all()
#     print(foods)
#     context = {"foods":foods}
#     return render(request,"index.html",context)

class IndexView(ListView):
    template_name = "food/index.html"
    context_object_name="foods"

    def get_queryset(self):
        return Food.objects.all()
