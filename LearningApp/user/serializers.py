from rest_framework import serializers
from .models import CustomUser

class UserCountSerializer(serializers.Serializer):
    user_count = serializers.IntegerField()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'location', 'about_me', 'short_description', 'university', 'profile_picture']

