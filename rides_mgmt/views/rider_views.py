from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets

from users.permissions import IsRiderUser
from ..serializers.find_customers import FindCustomerCardSerializer
from ..utils.db import find_customers


class FindCustomersViewSet(viewsets.ViewSet):
    serializer_class = FindCustomerCardSerializer
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsRiderUser]

    def get_queryset(self):
        return find_customers(self.request.user.rider)
