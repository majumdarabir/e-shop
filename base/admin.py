from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Customers
# Register your models here.


@admin.register(Customers)
class CustomersAdmin(ModelAdmin):
    pass
