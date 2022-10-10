from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


def some_time():
    current_datetime: datetime = timezone.now()
    return timezone.datetime(year=current_datetime.year-5, month=1, day=1)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=60, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    date_of_birth = models.DateField(default=some_time)
    image = models.ImageField(upload_to="profile", default="defaults/user.png")

    def __str__(self) -> str:
        return f"{self.user}"

 # implementation of profile change
