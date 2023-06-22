from django.urls import path
from django.urls.conf import include
from user import views
from .views import EndpointList, UserCountAPIView
from rest_framework.routers import DefaultRouter
userCount = DefaultRouter()
userCount.register(r'user-count', UserCountAPIView, basename='user-count')
urlpatterns = [
    path('', EndpointList.as_view()),
    
]+ userCount.urls
