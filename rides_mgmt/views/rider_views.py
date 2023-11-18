from dj_rest_auth.jwt_auth import JWTCookieAuthentication

from rest_framework import viewsets, status
from rest_framework.response import Response

from users.permissions import IsRiderUser
from ..models import RideObject
from ..serializers.find_customers import FindCustomerCardSerializer
from ..utils.db import find_customers


class FindCustomersViewSet(viewsets.ModelViewSet):
    serializer_class = FindCustomerCardSerializer
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsRiderUser]

    def get_queryset(self):
        if self.action == 'list':
            return find_customers(rider=self.request.user.rider)
        elif self.action == 'retrieve':
            return RideObject.objects.filter(id=self.kwargs.get('pk'), rider=self.request.user.rider)
        else:
            return RideObject.objects.none()

