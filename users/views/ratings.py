from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import UserRatingModel
from users.serializers import UserRatingSerializer


class UserRatingView(APIView):
    authentication_classes = [JWTCookieAuthentication]
    serializer_class = UserRatingSerializer

    def get(self, request):
        try:
            user_id = self.request.GET.get('user_id')
            user = UserRatingModel.objects.filter(rider=user_id)
            serializer = UserRatingSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = UserRatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
