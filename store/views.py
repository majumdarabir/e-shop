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
    review = Review.objects.get(pk=review_id)
    is_liked = review.liked_by.contains(request.user.customer)
    is_unliked = review.unliked_by.contains(request.user.customer)
    if is_unliked:
        review.liked_by.add(request.user.customer)
        review.unliked_by.remove(request.user.customer)
        return JsonResponse(
            {"like_class": "fa-solid fa-thumbs-up", 'unlike_class': "fa-regular fa-thumbs-down",
                "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )
    if not is_liked:
        review.liked_by.add(request.user.customer)
        return JsonResponse(
            {"like_class": "fa-solid fa-thumbs-up",
             "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )
    else:
        review.liked_by.remove(request.user.customer)
        return JsonResponse(
            {"like_class": "fa-regular fa-thumbs-up",
             "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )


@login_required
def favourite_item(request: HttpRequest, item_id: int):
    item = Item.objects.get(pk=item_id)
    is_userfavorite = item.favorite_users.contains(request.user.customer)
    if is_userfavorite:
        item.favorite_users.remove(request.user.customer)
        return JsonResponse({"fav_class": "btn btn-light btn-icon", "icon_class": "fa-regular fa-heart"})
    else:
        item.favorite_users.add(request.user.customer)
        return JsonResponse({"fav_class": "btn btn-secondary btn-icon", "icon_class": "fa-solid fa-heart"})


@login_required
def wishlist_item(request: HttpRequest, item_id: int):
    item = Item.objects.get(pk=item_id)
    is_wishlisted = item.wishlist_users.contains(request.user.customer)
    if is_wishlisted:
        item.wishlist_users.remove(request.user.customer)
        return JsonResponse({"is_wishlist": False})
    else:
        item.wishlist_users.add(request.user.customer)
        return JsonResponse({"is_wishlist": True})


@login_required
def unlike_review(request: HttpRequest, review_id: int):
    review = Review.objects.get(pk=review_id)
    is_liked = review.liked_by.contains(request.user.customer)
    is_unliked = review.unliked_by.contains(request.user.customer)
    if is_liked:
        review.liked_by.remove(request.user.customer)
        review.unliked_by.add(request.user.customer)
        return JsonResponse(
            {"like_class": "fa-regular fa-thumbs-up", 'unlike_class': "fa-solid fa-thumbs-down",
                "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )
    if not is_unliked:
        review.unliked_by.add(request.user.customer)
        return JsonResponse(
            {'unlike_class': "fa-solid fa-thumbs-down",
             "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )
    else:
        review.unliked_by.remove(request.user.customer)
        return JsonResponse(
            {'unlike_class': "fa-regular fa-thumbs-down",
             "un_like_count": review.unliked_by.count(), "like_count": review.liked_by.count()}
        )
