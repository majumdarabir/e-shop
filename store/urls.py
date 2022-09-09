from turtle import home
from django.urls import path
from .views.index import Index
from .views.login import Login
from .views.signup import Signup
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('signin', Login.as_view(), name='signup')
]
