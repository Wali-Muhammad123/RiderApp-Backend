from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from django.db import IntegrityError
from rest_framework import serializers

from users.serializers import CustomRegisterSerializer


# Create your views here.
class CustomLoginSerializer(DefaultLoginSerializer):
    username = None


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        try:
            user = serializer.save(self.request)
            super().perform_create(serializer)
        except IntegrityError:
            raise serializers.ValidationError("User registered Successfully")
