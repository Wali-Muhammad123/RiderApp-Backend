from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from users.models import RiderUser, Rider
from rest_framework.response import Response


@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_rider_bank(request):
    rider_id = request.GET.get("rider_id")
    if not rider_id:
        return Response({"message": "rider_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        rider = Rider.objects.get(id=rider_id)
        if not rider.bank_details:
            return Response({"message": "Rider has no bank account"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"bank_account": rider.bank_details}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        raise NotFound("Rider does not exist")
