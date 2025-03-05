from rest_framework import serializers

from . import models

# GET /users should serialize all user model properties
class UserSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

# POST /users should only expect the name property
class UserSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["name"]