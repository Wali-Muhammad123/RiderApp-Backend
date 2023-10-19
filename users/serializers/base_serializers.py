from rest_framework import serializers


class BaseRoleSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    current_location = serializers.SerializerMethodField(read_only=True)

    # rating = serializers.SerializerMethodField(read_only=True)

    def get_current_location(self, obj):
        try:
            return {
                'lat': obj.current_location.y,
                'lon': obj.current_location.x
            }
        except:
            return {
                'lat': None,
                'lon': None
            }

    def get_full_name(self, obj):
        return obj.full_name




