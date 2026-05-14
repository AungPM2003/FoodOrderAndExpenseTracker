from django.urls import path
from . import views

app_name="foodOrder"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("<int:food_id>/updateQuantity/",views.updateQuantity,name="updateQuantity"),
    path("cart/",views.CartView.as_view(),name="cart"),
    path("<int:food_id>/removeQuantity/",views.removeQuantity,name="removeQuantity")
]