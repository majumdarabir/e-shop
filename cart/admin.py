from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Cart, Orders


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    pass


@admin.register(Orders)
class OrdersAdmin(ModelAdmin):
    pass
