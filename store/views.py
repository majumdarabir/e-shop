from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, ReviewForms
from .models import Item, Like
from products.models import Category, Product


@login_required
def home(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    form = SearchForm
    return render(request, 'store/home.html', {"categories": categories, "form": form})


@login_required
def item_detailed(request: HttpRequest, pk: int) -> HttpResponse:
    product = Product.objects.get(pk=pk)
    item = Item.objects.get(product=product)

    return render(request, 'store/item_detailed.html', {"item": item, 'review_form': ReviewForms})


@login_required
def add_review_to_product(request: HttpRequest, item: int) -> HttpResponse:
    review = ReviewForms(request.POST)
    if review.is_valid():
        review.save()
    return redirect("item", item=item)


@login_required
def bookmark_a_product(request: HttpRequest) -> HttpResponse:
    return redirect("bookmark")
