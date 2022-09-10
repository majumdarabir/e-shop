from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customers(models.Model):
    user: models.Field = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at: models.Field = models.DateTimeField(auto_now_add=True)
    updated_at: models.Field = models.DateTimeField(auto_now=True)
