from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.exceptions import NotFound

from rides_mgmt.permissions import IsRiderUser


@api_view(['GET'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsRiderUser])
def get_customers_in_area(request):
    radius = request.GET.get('radius')
    