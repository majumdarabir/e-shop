from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from .models import Category, Product


@login_required
def show_categories(request: HttpRequest):
    category = Category.objects.all()
    return render(request, 'products/categories.html', {"categories": category})


@login_required
def show_products(request: HttpRequest):
    products = Product.objects.all()
    return render(request, 'products/products.html', {"products": products})


@login_required
def category_detailed(request: HttpRequest, pk: int):
    category = Category.objects.filter(pk=pk).first()

    return render(request, 'products/categories.html', {'category': category})
