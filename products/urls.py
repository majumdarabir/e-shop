from django.urls import path
from .views import (show_products, show_categories,
                    show_product_of_category, search, category_detailed)

urlpatterns = [
    path('', show_products, name="products"),
    path('search', search, name="search_product"),
    path('<int:category_id>', show_product_of_category,
         name="product-of-category"),
    path('categories', show_categories, name="categories"),
    path('categories/<int:pk>', category_detailed, name="category-detailed"),
]
