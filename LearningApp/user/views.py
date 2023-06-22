from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserCountSerializer
from rest_framework.viewsets import ViewSet

class EndpointList(APIView):
    def get(self, request):
        return Response({
            'authentication': {
                'sign up': 'http://127.0.0.1:8000/auth/users/',
                'log in(generate jwt token)': 'http://127.0.0.1:8000/auth/jwt/create',
                'current user': 'http://127.0.0.1:8000/auth/users/me/'
            },
        })
            
class UserCountAPIView(ViewSet):
    def list(self, request):
        user_count = CustomUser.objects.count()
        serializer = UserCountSerializer({"user_count": user_count})
        return Response(serializer.data)
