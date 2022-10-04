from django.urls import path
from .views import *

urlpatterns = [
    path('', show_products, name="products"),
    path('<int:category_id>', show_product_of_category,
         name="product-of-category"),
    path('categories', show_categories, name="categories"),
    path('categories/<int:pk>', category_detailed, name="category-detailed"),
]
