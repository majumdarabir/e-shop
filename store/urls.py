from turtle import home
from django.urls import path
from .views import home, item_detailed

urlpatterns = [
    path('', home, name='home'),
    path('item/<int:pk>', item_detailed, name="item_detailed"),
]
