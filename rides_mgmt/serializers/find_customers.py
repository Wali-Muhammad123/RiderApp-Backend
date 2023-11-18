from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from rides_mgmt.models import RideObject


class PickUpPointSerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RideObject
        geo_field = 'pickup_location'
        fields = ('pickup_location',)


class DropOffPointSerializer(gis_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RideObject
        geo_field = 'drop_off_location'
        fields = ('drop_off_location',)


class FindCustomerCardSerializer(serializers.ModelSerializer):
    # pickup_location = PickUpPointSerializer()
    # drop_off_location = DropOffPointSerializer()
    pickup_location = serializers.SerializerMethodField(read_only=True)
    drop_off_location = serializers.SerializerMethodField(read_only=True)
    customer = serializers.SerializerMethodField(read_only=True)
    demographics = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = RideObject
        fields = ('pickup_location', 'drop_off_location', 'deal_price', 'id', 'ride_id', 'customer', 'demographics')

    def get_customer(self, obj):
        return {
            'id': obj.customer.id,
            'full_name': obj.customer.full_name,
            'phone_number': obj.customer.phone_number,
        }

    def get_demographics(self, obj):
        try:
            # Ensure both locations are available
            if obj.pickup_location and obj.drop_off_location:
                distance = obj.pickup_location.distance(obj.drop_off_location)
                time = distance / 40  # Assuming a constant speed of 40 km/h
                return {'distance': distance, 'time': time}
            else:
                return {'distance': None, 'time': None}
        except Exception as e:
            # Handle potential errors (e.g., invalid location data)
            return {'error': str(e)}

    def get_pickup_location(self, obj):
        return {
            'type': 'Pickup Point',
            'coordinates': [obj.pickup_location.x, obj.pickup_location.y]
        }

    def get_drop_off_location(self, obj):
        return {
            'type': 'Drop Off Point',
            'coordinates': [obj.drop_off_location.x, obj.drop_off_location.y]
        }

