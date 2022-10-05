from django.contrib import admin

from .models import Item, Review


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
