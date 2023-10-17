from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rides_mgmt.serializers import PointSerializer

from rides_mgmt.utils.price_calculator import calculate_price


@api_view(['POST'])
@authentication_classes([IsAuthenticated])
def get_ride_price(request):
    ride_type = request.GET.get('ride_type')
    if ride_type == 'parcel':
        calc_price = calculate_price()