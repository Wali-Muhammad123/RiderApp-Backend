from rest_framework import serializers

from users.serializers.card_serializers import RiderCardSerializer


class FindRiderSerializer(serializers.Serializer):
    rider = serializers.SerializerMethodField(read_only=True)
    deal_price = serializers.SerializerMethodField(read_only=True)
    demographics = serializers.SerializerMethodField(read_only=True)

    def get_rider(self, obj):
        return RiderCardSerializer(obj.rider).data

    def get_demographics(self, obj):
        try:
            distance = obj.pickup_location.distance(obj.rider.current_location).km
            arrival_time = (distance / 40) * 60
            return {
                "distance": distance,
                "arrival_time": arrival_time
            }
        except:
            return None
    def get_deal_price(self, obj):
        return obj.deal_price