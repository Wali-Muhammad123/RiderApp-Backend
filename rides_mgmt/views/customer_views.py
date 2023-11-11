from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets

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

