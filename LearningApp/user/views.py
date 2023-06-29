from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserCountSerializer
from djoser.views import UserViewSet
class EndpointList(APIView):
    def get(self, request):
        return Response({
            'authentication': {
                'sign up': 'http://127.0.0.1:8000/auth/users/',
                'log in(generate jwt token)': 'http://127.0.0.1:8000/auth/jwt/create',
                'current user': 'http://127.0.0.1:8000/auth/users/me/',
                'password_rest' : 'http://127.0.0.1:8000/auth/users/reset_password/',
                'password_reset_confirmation': 'http://127.0.0.1:8000/auth/users/reset_password_confirm/'
            },
            'info' : {
                'user count': 'http://127.0.0.1:8000/user-count/'
            },
            'course' : {
                'course list' : 'http://127.0.0.1:8000/course/',
                'course instance': 'http://127.0.0.1:8000/course/<course_pk>',
                'course category' : 'http://127.0.0.1:8000/course/?category=<course category>'
            }
        })
            
class UserCountAPIView(APIView):
    def get(self, request):
        user_count = CustomUser.objects.count()
        serializer = UserCountSerializer({"user_count": user_count})
        return Response(serializer.data)

class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return render(request, "user/return.html")

def password_reset_confirm_view(request, uid, token):
    context = {
        'uid': uid,
        'token': token,
    }
    return render(request, 'user/password_reset_confirm.html', context)
