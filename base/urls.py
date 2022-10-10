from django.urls import path
from .views import (change_password, logout_user, register_user,
                    login_user, profile, delete_account)

urlpatterns = [
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name="logout"),
    path('profile', profile, name="profile"),
    path("delete-account", delete_account, name="delete-account"),
    path("change-password", change_password, name="change-password")
]
