from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from base.models import Customer
from .models import Cart


@receiver([post_save], sender=Customer)
def create_cart(sender, instance, created, **kwags):
    if created:
        Cart.objects.create(user=instance)
