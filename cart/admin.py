from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Cart, Coupon, Order, OrderedItem
from .forms import CartForm, CouponAdminForm


@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    form = CouponAdminForm
    list_display = 'code', 'valid', 'discount_amount'
    ordering = '-valid_till',
    list_filter = 'user',


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    form = CartForm
    list_display = "user", "updated_at", 'total_price', 'discount', 'final_price'
    ordering = "-created_at",
    list_filter = 'user', 'coupons'


@admin.register(OrderedItem)
class OrdersAdmin(ModelAdmin):
    list_display = "user", "item", 'item_price', 'item_count', 'total_price'
