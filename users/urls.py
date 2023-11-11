from django.urls import path
from .views import *


urlpatterns = [
    path('/rating', UserRatingView.as_view(), name='user_rating'),
    path('/update/profile/customer', update_customer_profile, name='update_talent_profile'),
    path('/update/profile/rider', update_customer_profile, name='update_talent_profile'),
    path('/get/profile/customer', update_customer_profile, name='update_talent_profile'),
    path('/get/profile/rider', update_customer_profile, name='update_talent_profile'),
    path('/update/availability/rider', update_rider_location_status, name='update_talent_profile'),
    path('/update/availability/customer', update_customer_location_status, name='update_talent_profile'),
]
