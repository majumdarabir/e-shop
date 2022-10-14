from django.urls import path
from .views import (cart, orders, checkout, checkcode,
                    remove_item_from_cart, refresh_item_count, add_item_to_cart)


urlpatterns = [
    path("", cart, name="cart"),
    path("orders", orders, name="orders"),
    path("checkout", checkout, name="checkout"),
    path("promo-code", checkcode, name="check-code"),
    path('add-cart', add_item_to_cart, name="add-to-cart"),
    path("remove-item/<int:item_id>",
         remove_item_from_cart, name="remove_item_cart"),
    path("update-item/<int:item>", refresh_item_count, name="update-item")
]
