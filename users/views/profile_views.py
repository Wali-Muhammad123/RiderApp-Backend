from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from ..permissions import IsRiderUser, IsCustomerUser
from ..serializers.profile_serializers import RiderSerializer, CustomerSerializer


@api_view(['PUT'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def update_rider_profile(request):
    rider = request.user.rider
    rider_profile = RiderSerializer(instance=rider, data=request.data, partial=True)
    if rider_profile.is_valid():
        rider_profile.save()
        return Response(rider_profile.data, status=status.HTTP_200_OK)
    return Response(rider_profile.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsCustomerUser])
def update_customer_profile(request):
    customer = request.user.customer
    customer_profile = CustomerSerializer(instance=customer, data=request.data, partial=True)
    if customer_profile.is_valid():
        customer_profile.save()
        return Response(customer_profile.data, status=status.HTTP_200_OK)
    return Response(customer_profile.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def get_rider_profile(request):
    rider = request.user.rider
    rider_profile = RiderSerializer(instance=rider)
    return Response(rider_profile.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsCustomerUser])
def get_customer_profile(request):
    customer = request.user.customer
    customer_profile = CustomerSerializer(instance=customer)
    return Response(customer_profile.data, status=status.HTTP_200_OK)
