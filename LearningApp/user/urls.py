from django.urls import path
from django.urls.conf import include
from user import views
from .views import EndpointList, UserCountAPIView, ActivateUser, password_reset_confirm_view
urlpatterns = [
    path('', EndpointList.as_view()),
    path('usercount/', UserCountAPIView.as_view()),
    path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('password/reset/confirm/<uid>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),

    
]
