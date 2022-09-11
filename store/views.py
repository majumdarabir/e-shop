from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from products.models import Category


def home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    categories = Category.objects.all()
    return render(request, 'store/home.html', {"categories": categories})
