from posixpath import basename
from django.urls import path
from django.urls.conf import include
from user import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import EndpointList, UserCountAPIView, ActivateUser, password_reset_confirm_view, CustomUserViewSet, EnrolledCoursesViewSet

router = routers.DefaultRouter()
router.register('user', CustomUserViewSet, basename='CustomUser')

nested_router = routers.NestedDefaultRouter(router, r'user', lookup='CustomUser')
nested_router.register('enrolledCourses', EnrolledCoursesViewSet, basename='enrolled-courses')

urlpatterns = [
    path('', EndpointList.as_view()),
    path('usercount/', UserCountAPIView.as_view()),
    path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('password/reset/confirm/<uid>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('',include(router.urls)),
    path('',include(nested_router.urls)),
    
]
