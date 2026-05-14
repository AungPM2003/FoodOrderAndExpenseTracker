from django.shortcuts import render,get_object_or_404
from django.http import request,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views.generic import ListView
from .models import Food,Cart
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

class CartView(ListView):
    template_name = "food/cart.html"
    context_object_name="cart_items"
    def get_queryset(self):
        return Cart.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        for item in context["cart_items"]:
            item.total = item.quantity * item.price
        return context
    

def updateQuantity(request,food_id):
    food = get_object_or_404(Food,pk=food_id)
    total_price = food.quantity * food.price
    if request.method == "POST":
        action = request.POST["action"]
        if action == "increase":
            food.quantity += 1
        elif action == "decrease" and food.quantity > 0:
            food.quantity -= 1
        elif action == "add" and food.quantity > 0:
            existing_cart = food.cart_set.filter(name=food.name).first()
            if existing_cart:
                existing_cart.quantity += food.quantity
                existing_cart.save()
            else:
                cart = food.cart_set.create(name=food.name,price=food.price,quantity=food.quantity)
                cart.save()
            food.quantity = 0
    food.save()
    return HttpResponseRedirect(reverse("foodOrder:index"))



def removeQuantity(request,food_id):
    food = get_object_or_404(Cart,pk=food_id)
    if request.method == "POST":
        action = request.POST['action']
        if action == "remove":
            food.quantity = 0
        food.delete()

    return HttpResponseRedirect(reverse("foodOrder:cart"))