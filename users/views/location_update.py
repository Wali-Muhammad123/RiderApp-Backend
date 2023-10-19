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
def update_rider_location(request):
    rider = request.user.rider
    rider.location = Point(request.data.get('longitude'), request.data.get('latitude'))
    rider.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated,IsCustomerUser])
def update_customer_location(request):
    customer = request.user.customer
    customer.location = Point(request.data.get('longitude'), request.data.get('latitude'))
    customer.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated,IsRiderUser])
def update_availability_status(request):
    if request.user.role == 'rider':
        rider = request.user.rider
        rider.status = request.data.get('is_available')
        rider.save()
        return Response(status=status.HTTP_200_OK)
    elif request.user.role == 'customer':
        customer = request.user.role
        customer.status = request.data.get('is_available')
        customer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
