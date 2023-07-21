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

from .models import Course, Module, Quiz, Question, PDF, VideoLecture, CourseReview, EnrolledStudent, Instructor, Module
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, PDFSerializer, VideoLectureSerializer, CourseReviewSerializer, EnrolledStudentSerializer, InstructorSerializer, ModuleSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category']

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class InstructorViewSet (ModelViewSet):
    #queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_queryset(self):
        course_id = self.kwargs['courses_pk']
        return Instructor.objects.filter(course_id=course_id)

class ModuleViewSet(ModelViewSet):
    #queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs['courses_pk']
        return Module.objects.filter(course_id=course_id)
    
    
class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuizSerializer

    def get_queryset(self):
        module_id = self.kwargs['module_pk']
        return Quiz.objects.filter(module_id=module_id)

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
    serializer_class = PDFSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        module_id = self.kwargs['module_pk']
        return PDF.objects.filter(module_id=module_id)

class VideoLectureViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoLectureSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        module_id = self.kwargs['module_pk']
        return VideoLecture.objects.filter(module_id=module_id)

class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    #permission_classes = [IsAuthenticated]

class EnrolledStudentViewSet(viewsets.ModelViewSet):
    queryset = EnrolledStudent.objects.all()
    serializer_class = EnrolledStudentSerializer