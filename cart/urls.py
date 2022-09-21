from django.urls import path
from .views import cart, orders, checkout


urlpatterns = [
    path("", cart, name="cart"),
    path("orders", orders, name="orders"),
    path("checkout", checkout, name="checkout"),

]
