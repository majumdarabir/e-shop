from products.models import Category, Product
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from .models import Item


@login_required
def home(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        categories = Category.objects.all()
        form = SearchForm
    if request.method == 'POST':
        pass

    return render(request, 'store/home.html', {"categories": categories, "form": form})


@login_required
def item_detailed(request: HttpRequest, pk: int) -> HttpResponse:
    product = Product.objects.get(pk=pk)
    item = Item.objects.get(product=product)
    return render(request, 'store/item_detailed.html', {"item": item})
