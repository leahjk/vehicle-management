from rest_framework import serializers
from .models import Vehicle,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "firstName",
            "lastName",
            "username",
            "phone_number",
            "dob",
        )

class VehicleSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source="owner",read_only=True)
    class Meta:
        model = Vehicle
        fields = (
            "type",
            "number_plate",
            "yom",
            "capacity",
            "owner",
            "updated_at",
            "user_detail"
        )
        read_only_fields = [
            "updated_at",
            "user_detail",
        ]
        extra_kwargs = {
            "owner": {"write_only": True}
        }

