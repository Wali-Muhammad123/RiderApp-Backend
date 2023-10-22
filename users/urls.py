from django.urls import path

from users.views import UserRatingView
from users.views.profile_views import update_customer_profile

urlpatterns = [
    path('/rating', UserRatingView.as_view(), name='user_rating'),
    path('update/profile/customer', update_customer_profile, name='update_talent_profile'),
    path('update/profile/rider', update_customer_profile, name='update_talent_profile'),
    path('get/profile/customer', update_customer_profile, name='update_talent_profile'),
    path('get/profile/rider', update_customer_profile, name='update_talent_profile'),
    path('update/location/rider', update_customer_profile, name='update_talent_profile'),
    path('update/location/customer', update_customer_profile, name='update_talent_profile'),
    path('update/availability/rider', update_customer_profile, name='update_talent_profile'),
    path('update/availability/customer', update_customer_profile, name='update_talent_profile'),
]
