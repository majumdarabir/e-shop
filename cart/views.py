from email import message
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.validators import item_count_ge_zero
from store.models import Item

from .models import Cart, Coupon, OrderedItem
from .forms import CouponForm


@login_required
def cart(request: HttpRequest) -> HttpResponse:
    cart = Cart.objects.get(user__user=request.user)
    coupon_form = CouponForm
    return render(request, "cart/cart.html", {"cart": cart, "coupon_form": coupon_form})


@login_required
def orders(request: HttpRequest) -> HttpResponse:
    return render(request, "cart/orders.html")


@login_required
def checkout(request: HttpRequest) -> HttpResponse:
    return render(request, "cart/checkout.html")


@login_required
def refresh_item_count(request: HttpRequest, item: int) -> HttpResponse:
    item_count = request.POST.get("item_count")
    item = request.POST.get("item_id")
    order_item = OrderedItem.objects.filter(
        item__id=item, user__user=request.user)
    if not order_item:
        messages.error(request, "This item don't exist in the cart")
        return redirect("cart")
    order_item.update(item_count=item_count)
    messages.success(
        request, message=f"Ordereing {order_item.first().item_count}x{order_item.first().item} ")
    return redirect("cart")


@login_required
def add_item_to_cart(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        item = request.POST.get("item_id" or None)
        item_count = request.POST.get("item_count" or 1)
        cart = Cart.objects.get(user__user=request.user)
        order_item_exits = OrderedItem.objects.filter(
            item__id=item, user__user=request.user).first()
        if order_item_exits:
            messages.warning(
                request, f"{order_item_exits.item} is already in the cart.Ypu may increase or decrease qualities form here")
        else:
            item_model = Item.objects.get(pk=item)
            order = OrderedItem.objects.create(
                item=item_model, user=request.user.customer, item_count=item_count)
            cart.items.add(order)
            messages.success(request, f"{order.item} added to cart")
    return redirect("cart")


@login_required
def checkcode(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        coupon_form = CouponForm(request.POST)
        if not coupon_form.is_valid():
            messages.error(request, coupon_form.errors)
            return redirect("cart")
        code = coupon_form.data['code']
        valid_code = Coupon.objects.filter(code=code).first()
        if valid_code:
            if not valid_code.valid:
                messages.error(request, "Coupon expired!!")
                return redirect("cart")
            if valid_code.user.contains(request.user.customer):
                messages.warning(request, "Already used the code")
                return redirect("cart")
            valid_code.user.add(request.user.customer)
            cart = Cart.objects.get(user=request.user.customer)
            cart.coupons.add(valid_code)
            messages.success(request, "Coupon applied")
            return redirect("cart")
        messages.warning(request, f"{code}:Invalid code")
    return redirect("cart")


@login_required
def remove_item_from_cart(request: HttpRequest, item_id: int) -> HTTPResponse:
    item = OrderedItem.objects.get(item__id=item_id)
    cart = Cart.objects.get(user__user=request.user)
    if item.user != cart.user:
        messages.error(request, "Permission denied")
    if not cart.items.contains(item):
        messages.warning(request, "Item don't belong to the cart")
        return redirect("cart")
    cart.items.remove(item)
    item.delete()
    messages.success(request, f"Removed {item.product} from your cart")
    return redirect("cart")
