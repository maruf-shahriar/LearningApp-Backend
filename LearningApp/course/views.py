from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Course, Quiz, Question, PDF, VideoLecture, CourseReview, EnrolledStudent
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, PDFSerializer, VideoLectureSerializer, CourseReviewSerializer, EnrolledStudentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category', 'instructor']

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
    
class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    #permission_classes = [IsAuthenticated]

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def update(self, request, *args, **kwargs):
        question = self.get_object()
        is_correct = request.data.get('is_correct')
        
        if is_correct is not None:
            question.is_correct = is_correct
            question.save()
            return Response(QuestionSerializer(question).data)
        else:
            return Response({'error': 'is_correct field is missing or invalid'}, status=status.HTTP_400_BAD_REQUEST)

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

class EnrolledStudentViewSet(viewsets.ModelViewSet):
    queryset = EnrolledStudent.objects.all()
    serializer_class = EnrolledStudentSerializer