from django.contrib import admin

from products.models import Product
from .models import Item, Review, WishList, Favourite


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(WishList)
class BookMarkAdmin(admin.ModelAdmin):
    pass


@admin.register(Favourite)
class LikeAdmin(admin.ModelAdmin):
    pass
