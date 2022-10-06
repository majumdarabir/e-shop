from turtle import home
from django.urls import path
from .views import (home, item_detailed, add_review_to_product,
                    like_review, unlike_review, favourite_item, wishlist_item, user_favourites, user_wishlist)

urlpatterns = [
    path('', home, name='home'),
    path('wishlist', user_wishlist, name="wishlist"),
    path('favourite', user_favourites, name="favourites"),
    path('item/<int:pk>', item_detailed, name="item_detailed"),
    path('add-comment/<int:item_id>', add_review_to_product, name="add-commnet"),
    path('like-review/<int:review_id>', like_review, name="like-review"),
    path('unlike-review/<int:review_id>', unlike_review, name="unlike-review"),
    path('favorite-item/<int:item_id>', favourite_item, name="favorite-item"),
    path('wishlist-item/<int:item_id>', wishlist_item, name="wishlist-item")
]
