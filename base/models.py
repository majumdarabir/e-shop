from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="profile", default="defaults/user.png")

    def __str__(self) -> str:
        return f"{self.user}"

 # implementation of profile change
