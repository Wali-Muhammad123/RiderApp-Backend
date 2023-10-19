from rest_framework import serializers

from users.models import UserRatingModel
from users.serializers.base_serializers import BaseRoleSerializer


class CustomerCardSerializer(BaseRoleSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    def get_rating(self, obj):
        try:
            rating = (
                UserRatingModel.objects.filter(customer=obj).aggregate(avg_rating=Avg('rating')).get('avg_rating'))
            return rating
        except Exception as e:
            return 0


class RiderCardSerializer(BaseRoleSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    def get_rating(self, obj):
        try:
            rating = (
                UserRatingModel.objects.filter(rider=obj).aggregate(avg_rating=Avg('rating')).get('avg_rating'))
            return rating
        except Exception as e:
            return 0
