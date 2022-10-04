from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Category, Product
from .forms import PricePickerForm


def search(request: HttpRequest) -> HttpResponse:
    pass


def show_categories(request: HttpRequest) -> HttpResponse:
    category = Category.objects.all()
    return render(request, 'products/categories.html', {"categories": category})


def show_products(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        products = Product.objects.all()
        categories = Category.objects.all()
        return render(request, 'products/products.html', {
            "products": products,
            "categories": categories,
            "price_form": PricePickerForm
        })
    if request.method == "POST":
        return render(request, 'products/products.html', {
            "products": products,
            "categories": categories,
            "price_form": PricePickerForm
        })


def show_product_of_category(request: HttpRequest, category_id: int) -> HttpResponse:
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'products/products.html', {
        "products": category.product_set.all(),
        "current_category": category,
        "categories": categories
    })


def category_detailed(request: HttpRequest, pk: int) -> HttpResponse:
    category = Category.objects.filter(pk=pk).first()
    return render(request, 'products/categories.html', {'category': category})
