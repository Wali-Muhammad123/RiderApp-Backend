from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..permissions import IsRiderUser, IsCustomerUser


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def update_rider_location_status(request):
    rider = request.user.rider
    rider.location = Point(request.data.get('lon'), request.data.get('lat'))
    rider.status = 'available'
    rider.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated,IsCustomerUser])
def update_customer_location_status(request):
    customer = request.user.customer
    customer.location = Point(request.data.get('lon'), request.data.get('lat'))
    customer.status = 'available'
    customer.save()
    return Response(status=status.HTTP_200_OK)

