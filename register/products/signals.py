from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Products

@receiver(post_save, sender=Products)
def create_handler(sender, instance, created, **kwargs):
    if created:
        print("Successfully created:", instance.name)

@receiver(pre_delete, sender=Products)
def delete_handler(sender, instance, **kwargs):
    print("Successfully deleted:", instance.name)
