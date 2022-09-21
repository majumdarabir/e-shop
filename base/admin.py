from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Customer
# Register your models here.


@admin.register(Customer)
class CustomersAdmin(ModelAdmin):
    pass
