from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import BuyerProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        BuyerProfile.objects.create(buyer=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.buyerprofile.save()
