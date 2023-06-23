from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import QuizViewSet, PDFViewSet, VideoLectureViewSet, CourseReviewViewSet, CourseViewSet, CourseEnrollView
router = routers.DefaultRouter()
router.register('', CourseViewSet, basename='courses')

nested_router = routers.NestedDefaultRouter(router, r'', lookup='courses')
nested_router.register('pdf', PDFViewSet, basename='course-pdf')
nested_router.register('quiz', QuizViewSet, basename='course-quiz')
nested_router.register('video', VideoLectureViewSet, basename='course-video')
nested_router.register('course-review', CourseReviewViewSet, basename='course-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('<int:course_id>/enroll/', CourseEnrollView.as_view(), name='course-enroll'),
    #path('course/<int:course_id>/enroll/<int:pk>/', CourseEnrollView.as_view(), name='course-enroll-detail'),
]
