from rest_framework import serializers


class FindCustomerSerializer(serializers.Serializer):
    customer = serializers.SerializerMethodField(read_only=True)
    current_location = serializers.SerializerMethodField(read_only=True)
    # distance = serializers.SerializerMethodField(read_only=True)
    price_calculated = serializers.SerializerMethodField(read_only=True)

    def get_customer(self, obj):
        ...  # Add here customer serializer

    def get_current_location(self, obj):
        return {
            'lat': obj.current_location.y,
            'lon': obj.current_location.x
        }
