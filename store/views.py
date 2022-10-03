from django.http import HttpRequest, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SearchForm, ReviewForms
from .models import Item, Review
from products.models import Category


@login_required
def home(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    form = SearchForm
    return render(request, 'store/home.html', {"categories": categories, "form": form})


@login_required
def item_detailed(request: HttpRequest, pk: int) -> HttpResponse:
    item = Item.objects.get(pk=pk)
    return render(request, 'store/item_detailed.html', {"item": item, 'review_form': ReviewForms})


@login_required
def categorized_products(request: HttpRequest, category_id: int) -> HttpResponse:
    category = Category.objects.get(pk=category_id)
    return render(request, 'products/categorized_product.html', {'products': category})


@login_required
def add_review_to_product(request: HttpRequest, item_id: int) -> HttpResponse:
    review = request.POST.get("review" or None)
    ratings = request.POST.get("ratings" or None)
    review_form = ReviewForms(
        data={"review": review, "ratings": ratings, "user": request.user.customer, "product": item_id})
    if review_form.is_valid():
        review_form.save()
        messages.success(request, "Your Review has been added 😆")
    else:
        messages.error(request, review_form.errors)
    return redirect("item_detailed", pk=item_id)


@login_required
def like_review(request: HttpRequest, review_id: int):
    liked_by = Review.objects.get(pk=review_id).liked_by
    is_already_liked = liked_by.contains(request.user.customer)
    if not is_already_liked:
        liked_by.add(request.user.customer)
        return JsonResponse({"like_count": liked_by.count()})
    else:
        return JsonResponse({"detail": "Already liked by the user"}, status=400)


@login_required
def unlike_review(request: HttpRequest, review_id):
    unliked_by = Review.objects.get(pk=review_id).unliked_by
    is_already_unliked = unliked_by.contains(request.user.customer)
    if not is_already_unliked:
        unliked_by.add(request.user.customer)
        return JsonResponse({"un_like_count": unliked_by.count()})
    else:
        return JsonResponse({"detail": "Already unliked by the user"}, status=400)


@login_required
def bookmark_a_product(request: HttpRequest) -> HttpResponse:
    return redirect("bookmark")
