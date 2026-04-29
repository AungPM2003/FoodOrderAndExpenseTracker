from django.shortcuts import render,get_object_or_404
from django.http import request,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
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

def updateQuantity(request,food_id):
    food = get_object_or_404(Food,pk=food_id)
    if request.method == "POST":
        action = request.POST["action"]
        
        if action == "increase":
            food.quantity = F('quantity') + 1
        elif action == "decrease" and food.quantity > 0:
            food.quantity = F('quantity') - 1
        elif action == "add" and food.quantity >= 0:
            pass
    food.save()
    return HttpResponseRedirect(reverse("foodOrder:index"))