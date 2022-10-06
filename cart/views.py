from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Cart


def cart(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        pass

    cart = Cart.objects.filter(user__user=request.user)
    print(cart)
    return render(request, "cart/cart.html", {"cart": cart})


def orders(request: HttpRequest) -> HttpResponse:
    return render(request, "cart/orders.html")


def checkout(request: HttpRequest) -> HttpResponse:
    return render(request, "cart/checkout.html")
