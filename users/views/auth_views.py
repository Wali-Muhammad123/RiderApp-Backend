from allauth.account import app_settings as allauth_account_settings
from allauth.account.utils import complete_signup
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.utils import jwt_encode
from rest_framework import serializers

from users.serializers import CustomRegisterSerializer


# Create your views here.



class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        try:
            user = serializer.save(self.request)
            if allauth_account_settings.EMAIL_VERIFICATION != \
                    allauth_account_settings.EmailVerificationMethod.MANDATORY:
                if api_settings.USE_JWT:
                    self.access_token, self.refresh_token = jwt_encode(user)
                elif not api_settings.SESSION_LOGIN:
                    # Session authentication isn't active either, so this has to be
                    #  token authentication
                    api_settings.TOKEN_CREATOR(self.token_model, user, serializer)
            complete_signup(
                self.request._request, user,
                allauth_account_settings.EMAIL_VERIFICATION,
                None,
            )
            return user
        except:
            raise serializers.ValidationError({'email': 'Email already exists'})
