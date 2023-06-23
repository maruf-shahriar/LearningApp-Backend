from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserCountSerializer
class EndpointList(APIView):
    def get(self, request):
        return Response({
            'authentication': {
                'sign up': 'http://127.0.0.1:8000/auth/users/',
                'log in(generate jwt token)': 'http://127.0.0.1:8000/auth/jwt/create',
                'current user': 'http://127.0.0.1:8000/auth/users/me/'
            },
            'info' : {
                'user count': 'http://127.0.0.1:8000/user-count/'
            }
        })
            
class UserCountAPIView(APIView):
    def get(self, request):
        user_count = CustomUser.objects.count()
        serializer = UserCountSerializer({"user_count": user_count})
        return Response(serializer.data)
