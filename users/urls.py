from django.urls import path

from users.views import UserRatingView

urlpatterns = [
    path('/rating', UserRatingView.as_view(), name='user_rating'),
]