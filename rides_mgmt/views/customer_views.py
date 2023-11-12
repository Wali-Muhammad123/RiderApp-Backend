from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.permissions import IsCustomerUser
from ..pagination import RidesPagination
from ..serializers.find_riders import FindRiderSerializer
from ..models import RideObject


class ListRidersViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsCustomerUser]
    serializer_class = FindRiderSerializer
    pagination_class = RidesPagination

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'customer'):
            return RideObject.objects.filter(customer=user.customer).exclude(rider=None)
        else:
            return RideObject.objects.none()

    @action(detail=True, methods=['post'])
    def book_ride(self, request, pk=None):
        ride = self.get_object()
        ride.ride_booked = True
        ride.rider.status = 'on_ride'
        ride.customer.status = 'on_ride'
        ride.save()
        ride.rider.save()
        ride.customer.save()
        return Response({"detail": "Ride Booked"}, status=status.HTTP_200_OK)
