import uuid
from django.db import models
from django.contrib.gis.db import models as gis_models
from users.models import Rider, Customer


# Create your models here.
class RideObject(models.Model):
    objects = models.Manager()
    TYPE = (
        ('ride', 'ride'),
        ('parcel', 'parcel')
    )
    id = models.BigAutoField(primary_key=True)
    ride_id = models.UUIDField(default=uuid.uuid4, editable=False)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    pickup_location = gis_models.PointField(null=True, blank=True)
    drop_off_location = gis_models.PointField(null=True, blank=True)
    pickup_time = models.DateTimeField(null=True, blank=True)
    drop_off_time = models.DateTimeField(null=True, blank=True)
    deal_price = models.IntegerField(null=True, blank=True)
    ride_booked = models.BooleanField(default=False)
