from turtle import home
from django.urls import path
from .views import home, item_detailed, add_review_to_product, bookmark_a_product, like_review, unlike_review

urlpatterns = [
    path('', home, name='home'),
    path('item/<int:pk>', item_detailed, name="item_detailed"),
    path('add-comment/<int:item_id>',
         add_review_to_product, name="add-commnet"),
    path('bookmark', bookmark_a_product, name="bookmark"),
    path('like-review/<int:review_id>', like_review, name="like-review"),
    path('unlike-review/<int:review_id>', unlike_review, name="unlike-review"),
]
