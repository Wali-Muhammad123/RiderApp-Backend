from rest_framework import serializers

from users.models import UserRatingModel


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatingModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
