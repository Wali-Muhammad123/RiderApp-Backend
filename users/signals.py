from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import RiderUser, Rider, Customer


@receiver(post_save, sender=RiderUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'rider':
            rider, created = Rider.objects.get_or_create(user=instance)
        elif instance.role == 'customer':
            customer, created = Customer.objects.get_or_create(user=instance)
        else:
            pass

