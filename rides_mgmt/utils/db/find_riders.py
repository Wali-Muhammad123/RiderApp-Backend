from django.contrib.gis.db.models.functions import Distance

from rides_mgmt.models import RideObject
from users.models import Customer


def find_customers(rider, radius=5000):
    """
    Find all customers within a specific radius
    :param rider:
    :param radius:
    :return: Customers within a specific radius
    """
    print(rider.current_location)
    nearby_rides = RideObject.objects.filter(
        pickup_location__distance_lte=(
            rider.current_location,
            radius
        ),
        pickup_location__isnull=False,  # Ensure drop_off_location is not None
        drop_off_location__isnull=False,  # Ensure pickup_location is not None
        ride_booked=False
    )
    if not nearby_rides:
        return None
    return nearby_rides
