import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.gis.db import models as gis_models
from django.db import models

from users.managers import RiderUserManager


#
class RiderUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('customer', 'customer'),
        ('admin', 'admin'),
        ('rider', 'rider')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    objects = RiderUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]


class BaseUserClass(models.Model):
    """
    Base class for Rider and Customer details
    """
    STATUS_CHOICES = (
        ('available', 'available'),
        ('unavailable', 'unavailable'),
        ('on_ride', 'on_ride')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(RiderUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    bank_details = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unavailable')
    current_location = gis_models.PointField(blank=True, null=True)

    class Meta:
        abstract = True


class Rider(BaseUserClass):
    objects = models.Manager()
    license = models.CharField(max_length=100, blank=True, null=True)
    vehicle = models.CharField(max_length=100, blank=True, null=True)


class Customer(BaseUserClass):
    objects = models.Manager()


class UserRatingModel(models.Model):
    objects = models.Manager()
    customer = models.ForeignKey(RiderUser, on_delete=models.PROTECT, related_name='customer_rating')
    rider = models.ForeignKey(RiderUser, on_delete=models.PROTECT, related_name='rider_rating')
    rating = models.IntegerField(default=5)
    review = models.CharField(max_length=100, blank=True, null=True)
