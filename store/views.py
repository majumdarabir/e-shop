from products.models import Category
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import SearchForm
from.models import Item


def home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == 'GET':
        categories = Category.objects.all()
        form = SearchForm

    return render(request, 'store/home.html', {"categories": categories, "form": form})


def item_detailed(request: HttpRequest, pk: int):
    item = Item.objects.get(pk=pk)
