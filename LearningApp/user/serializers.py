from rest_framework import serializers
from .models import CustomUser
class UserCountSerializer(serializers.Serializer):
    user_count = serializers.IntegerField()