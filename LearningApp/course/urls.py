from posixpath import basename
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import QuizViewSet, PDFViewSet, VideoLectureViewSet, CourseReviewViewSet, CourseViewSet, QuestionViewSet, EnrolledStudentViewSet

router = routers.DefaultRouter()
router.register('', CourseViewSet, basename='courses')

nested_router = routers.NestedDefaultRouter(router, r'', lookup='courses')
nested_router.register('pdf', PDFViewSet, basename='course-pdf')
nested_router.register('quiz', QuizViewSet, basename='course-quiz')
nested_router.register('video', VideoLectureViewSet, basename='course-video')
nested_router.register('CourseReview', CourseReviewViewSet, basename='course-review')
nested_router.register('EnrolledStudent', EnrolledStudentViewSet, basename = 'enrolled-student')

quiz_router = routers.NestedSimpleRouter(nested_router, r'quiz', lookup='quiz')
quiz_router.register('question', QuestionViewSet, basename='quiz-question')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(quiz_router.urls)),
]
