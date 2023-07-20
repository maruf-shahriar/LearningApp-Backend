from posixpath import basename
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import QuizViewSet, PDFViewSet, VideoLectureViewSet, CourseReviewViewSet, CourseViewSet, QuestionViewSet, EnrolledStudentViewSet, ModuleViewSet, InstructorViewSet

router = routers.DefaultRouter()
router.register('', CourseViewSet, basename='courses')

nested_router = routers.NestedDefaultRouter(router, r'', lookup='courses')
nested_router.register('instructor', InstructorViewSet, basename = 'instructor')
nested_router.register('module', ModuleViewSet, basename='module')
nested_router.register('CourseReview', CourseReviewViewSet, basename='course-review')
nested_router.register('EnrolledStudent', EnrolledStudentViewSet, basename = 'enrolled-student')

module_router = routers.NestedSimpleRouter(nested_router, r'module', lookup='module')
module_router.register('quiz', QuizViewSet, basename='quiz')
module_router.register('pdf', PDFViewSet, basename='pdf')
module_router.register('video', VideoLectureViewSet, basename='video-lecture')

quiz_router = routers.NestedSimpleRouter(module_router, r'quiz', lookup='quiz')
quiz_router.register('question', QuestionViewSet, basename='quiz-question')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(module_router.urls)),
    path('', include(quiz_router.urls)),
]
