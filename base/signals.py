from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from .models import Customer


@receiver([post_save], sender=User)
def create_customer(sender, instance, created, **kwags):
    if created:
        Customer.objects.create(user=instance)
