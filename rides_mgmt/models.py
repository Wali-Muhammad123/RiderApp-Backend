import uuid
from django.db import models
from django.contrib.gis.db import models as gis_models
from users.models import Rider, Customer


# Create your models here.
class RideObject(models.Model):
    TYPE = (
        ('ride', 'ride'),
        ('parcel', 'parcel')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pickup_location = gis_models.PointField()
    drop_off_location = gis_models.PointField()
    pickup_time = models.DateTimeField()
    drop_off_time = models.DateTimeField()
    deal_price = models.IntegerField()
