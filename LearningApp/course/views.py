from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import Prefetch
from rest_framework.views import APIView

from .models import Course, Quiz, PDF, VideoLecture, CourseReview, EnrolledStudent
from .serializers import CourseSerializer, QuizSerializer, PDFSerializer, VideoLectureSerializer, CourseReviewSerializer, EnrolledStudentSerializer
from user.models import CustomUser


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category']
    #permission_classes = [IsAuthenticated]

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    #permission_classes = [IsAuthenticated]

class PDFViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    #permission_classes = [IsAuthenticated]

class VideoLectureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoLecture.objects.all()
    serializer_class = VideoLectureSerializer
    #permission_classes = [IsAuthenticated]

class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    #permission_classes = [IsAuthenticated]

class CourseEnrollView(APIView):
    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"message": "Course not found"}, status=404)
        
        enrolled_students = EnrolledStudent.objects.filter(course=course)
        serializer = EnrolledStudentSerializer(enrolled_students, many=True)
        
        return Response(serializer.data)

    def post(self, request, course_id):
        username = request.data.get('username')
        email = request.data.get('email')

        try:
            course = Course.objects.get(id=course_id)
            user = CustomUser.objects.get(username=username, email=email)
        except (Course.DoesNotExist, CustomUser.DoesNotExist):
            return Response(status=400, data={'message': 'Invalid course or user'})

        enrolled_student = EnrolledStudent.objects.create(course=course, user=user)
        serializer = EnrolledStudentSerializer(enrolled_student)
        return Response(serializer.data)

    
    def delete(self, request, course_id, student_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"message": "Course not found"}, status=404)

        try:
            enrolled_student = EnrolledStudent.objects.get(course=course, student_id=student_id)
        except EnrolledStudent.DoesNotExist:
            return Response({"message": "Enrolled student not found"}, status=404)
        
        enrolled_student.delete()
        return Response({"message": "Enrollment removed"}, status=204)