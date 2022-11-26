from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Product, Stars, Digital, Physical, Price


@receiver(post_save, sender=Product)
def create_star_field(sender, instance, created, **kwargs):
    if created:
        Stars.objects.create(product=instance)
        Price.objects.create(product=instance)
        if instance.mode == 'physical':
            Physical.objects.create(product=instance)
        else:
            Digital.objects.create(product=instance)
