from django.contrib.gis.db.models.functions import Distance

from users.models import Customer


def find_customers(rider, radius=5000):
    """
    Find all customers within a specific radius
    :param rider:
    :param radius:
    :return: Customers within a specific radius
    """
    nearby_customers = Customer.objects.annotate(
        distance=Distance('current_location', rider.current_location)
    ).filter(distance_lte=radius, status='available').order_by('distance')
    return nearby_customers
