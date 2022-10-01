from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SearchForm, ReviewForms
from .models import Item
from products.models import Category


@login_required
def home(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    form = SearchForm
    return render(request, 'store/home.html', {"categories": categories, "form": form})


@login_required
def item_detailed(request: HttpRequest, pk: int) -> HttpResponse:
    item = Item.objects.get(product_id=pk)
    return render(request, 'store/item_detailed.html', {"item": item, 'review_form': ReviewForms})


@login_required
def add_review_to_product(request: HttpRequest, item_id: int) -> HttpResponse:
    review_form = ReviewForms(data={"user": request.user, **request.POST})
    if review_form.is_valid():
        review_form.save()
    else:
        print(review_form.errors)
        messages.warning(request, review_form.errors)
    return redirect("home")


@login_required
def bookmark_a_product(request: HttpRequest) -> HttpResponse:
    return redirect("bookmark")
