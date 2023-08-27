from posixpath import basename
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import (QuizViewSet, PDFViewSet, VideoLectureViewSet, CourseReviewViewSet, CourseViewSet, 
                    QuestionViewSet, ModuleViewSet, InstructorViewSet, CourseEnrollmentViewSet, QuizAttemptViewSet,
                    InstructorCoursesViewSet, PdfSeenViewSet, VideoWatchViewSet)

router = routers.DefaultRouter()
router.register('', CourseViewSet, basename='courses')

nested_router = routers.NestedDefaultRouter(router, r'', lookup='courses')
nested_router.register('instructor', InstructorViewSet, basename = 'instructor')
nested_router.register('module', ModuleViewSet, basename='module')
nested_router.register('CourseReview', CourseReviewViewSet, basename='course-review')
nested_router.register('enrollment', CourseEnrollmentViewSet, basename='course-enrollment')

module_router = routers.NestedSimpleRouter(nested_router, r'module', lookup='module')
module_router.register('quiz', QuizViewSet, basename='quiz')
module_router.register('pdf', PDFViewSet, basename='pdf')
module_router.register('video', VideoLectureViewSet, basename='videolecture')

quiz_router = routers.NestedSimpleRouter(module_router, r'quiz', lookup='quiz')
quiz_router.register('question', QuestionViewSet, basename='quiz-question')
quiz_router.register('quizAttempt', QuizAttemptViewSet, basename='quiz-attempt')

pdf_router = routers.NestedSimpleRouter(module_router, r'pdf', lookup='pdf')
pdf_router.register('pdf_seen', PdfSeenViewSet, basename='pdf-seen')

video_router = routers.NestedSimpleRouter(module_router, r'video', lookup='videolecture')
video_router.register('video_watch', VideoWatchViewSet, basename='video-watch')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(module_router.urls)),
    path('', include(quiz_router.urls)),
    path('', include(pdf_router.urls)),
    path('', include(video_router.urls)),
    path('teacher/<int:instructor_pk>/teachings/', InstructorCoursesViewSet.as_view({'get': 'list'}), name='instructor-courses'),
]
