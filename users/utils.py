from django.db.models import Avg

from .models import UserRatingModel


def get_average_rating_rider(customer):
    try:
        rating = (UserRatingModel.objects.filter(rider=customer).aggregate(avg_rating=Avg('rating')).get('avg_rating'))
        return rating
    except Exception as e:
        return 0