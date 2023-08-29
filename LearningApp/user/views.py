from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework import viewsets
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import CustomUser
from .serializers import UserCountSerializer, CustomUserSerializer

from course.models import Course
from course.serializers import CourseSerializer


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
            'course' : {
                'course list' : 'http://127.0.0.1:8000/course/',
                'course instance': 'http://127.0.0.1:8000/course/<course_pk>',
                'course category' : 'http://127.0.0.1:8000/course/?category=<course_category>',
                'course search' : 'http://127.0.0.1:8000/course/?search=<course_title, course_instructor>',
                'course instructor': 'http://127.0.0.1:8000/course/<course_pk>/instructor',
                'course enrollment (students who are enrolled) POST' : 'http://127.0.0.1:8000/course/<course_pk>/enrollment/',
                'course module' : 'http://127.0.0.1:8000/course/<course_pk>/module/',
                'course quiz': 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/quiz/',
                'course quiz attempt (attempted by users)' : 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/quiz/<quiz_pk>/quizAttempt/',
                'course quiz question': 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/quiz/<quiz_pk>/question',
                'course pdf': 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/pdf',
                'course pdf seen': 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/pdf/<pdf_pk>/pdf_seen/',
                'course video' : 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/video',
                'course video watched' : 'http://127.0.0.1:8000/course/<course_pk>/module/<module_pk>/video/<video_pk>/video_watch/'
            },

            'user':{
                'user' : 'http://127.0.0.1:8000/user/',
                'user instance' : 'http://127.0.0.1:8000/user/<user_pk>/',
                'enrolled courses (user enrolled courses)':'http://127.0.0.1:8000/user/<user_id>/enrolledCourses/',
            },

            'instructor': {
                'instructor teachings': 'http://127.0.0.1:8000/course/teacher/<instructor_id>/teachings/',
            },

            'info' : {
                'user count': 'http://127.0.0.1:8000/user-count/'
            },
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

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    
class EnrolledCoursesViewSet (viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    def get_queryset(self):
        user_id = self.kwargs['CustomUser_pk']
        #user = User.objects.get(id=user_id)
        enrolled_courses = Course.objects.filter(students=user_id)
        return enrolled_courses

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        subject = f"New Contact Message from {name}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        message_format = f"Name: {name}\nEmail: {email}\nMessage: {message}"


        try:
            send_mail(subject, message_format, from_email, recipient_list)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error sending email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        