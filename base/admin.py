from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = "user", "first_name", 'last_name', 'email',
    ordering = "-created_at",
