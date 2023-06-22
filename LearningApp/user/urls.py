from django.urls import path
from django.urls.conf import include
from user import views
from .views import EndpointList
urlpatterns = [
    path('', EndpointList.as_view())
]
