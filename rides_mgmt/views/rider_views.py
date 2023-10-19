from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import NotFound
from ..utils.db import find_customers

from users.permissions import IsRiderUser


@api_view(['GET'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def get_customers_in_area(request):
    radius = request.GET.get('radius')
    if not radius:
        get_customers = find_customers(request.user.rider)
    else:
        get_customers = find_customers(request.user.rider, radius)
        if not get_customers:
            raise NotFound('No customers found in the area')


    