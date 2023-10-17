from django.conf import settings
from django.contrib.gis.geos import Point


def calculate_price(pickup_location, drop_off_location, price_set=settings.RIDE_PRICE_PER_KM):
    pickup_point = Point(pickup_location.get('lon'), pickup_location.get('lat'))
    drop_off_point = Point(drop_off_location.get('lon'), drop_off_location.get('lat'))
    distance = pickup_point.distance(drop_off_point) / 1000
    total_ride_price = distance * price_set
    return total_ride_price


