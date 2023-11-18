from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rides_mgmt.models import RideObject
from ..permissions import IsRiderUser, IsCustomerUser


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def update_rider_location_status(request):
    rider = request.user.rider
    rider.location = Point(request.data.get('lon'), request.data.get('lat'))
    rider.status = 'available'
    print(rider.location)
    rider.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated, IsCustomerUser])
def update_customer_location_status(request):
    customer = request.user.customer
    pickup = request.data.get('pickup')
    drop_off = request.data.get('drop_off')
    if not pickup or not drop_off:
        raise ValidationError("Pickup Location or Drop Location Not provided")
    drop_off_point = Point(drop_off.get('lon'), drop_off.get('lat'))
    pickup_point = Point(pickup.get('lon'), pickup.get('lat'))
    customer.location = pickup_point
    customer.status = 'available'
    create_ride = RideObject.objects.create(
        customer=customer,
        pickup_location=pickup_point,
        drop_off_location=drop_off_point
    )
    customer.save()
    return Response(data={
        "ride_id": create_ride.id
    }, status=status.HTTP_200_OK)
