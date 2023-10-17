from django.conf import settings
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
    pickup_point = request.data.get('pickup_point')
    drop_off_point = request.data.get('drop_off_point')
    if ride_type == 'parcel':
        calc_price = calculate_price(pickup_point, drop_off_point, price_set=settings.PRICE_PER_KM_PARCEL)
    else:
        calc_price = calculate_price(pickup_point, drop_off_point)
    return Response(
        {
            "price_est": calc_price
        }, status=status.HTTP_200_OK
    )


