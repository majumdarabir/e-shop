from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Cart, Order, OrderedItem, PromoCode
from .forms import CartForm

admin.site.register(OrderedItem)
admin.site.register(PromoCode)


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    form = CartForm
    list_display = "user", "updated_at"
    ordering = "-created_at",
    list_filter = 'user',


@admin.register(Order)
class OrdersAdmin(ModelAdmin):
    pass
