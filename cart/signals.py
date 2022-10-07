from django.dispatch import receiver
from django.db.models.signals import pre_save

from base.models import Customer
from .models import Cart


@receiver([pre_save], sender=Customer)
def create_cart(sender, instance, **kwags):
    Cart.objects.create(user=instance)
