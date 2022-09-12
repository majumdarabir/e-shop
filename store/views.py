from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import SearchForm
from products.models import Category


def home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == 'GET':
        categories = Category.objects.all()
        form = SearchForm

    return render(request, 'store/home.html', {"categories": categories, "form": form})
