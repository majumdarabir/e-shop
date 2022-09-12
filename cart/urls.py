from django.urls import path
from .views import cart, orders
urlpatterns = [
    path("", cart, name="cart"),
    path("orders", orders, name="orders")
]
