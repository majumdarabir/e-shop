from django.urls import path
from .views import category_detailed, show_products, show_categories
urlpatterns = [
    path('', show_products, name="products"),
    path('categories', show_categories, name="categories"),
    path('categories/<int:pk>', category_detailed, name="category-detailed")
]
