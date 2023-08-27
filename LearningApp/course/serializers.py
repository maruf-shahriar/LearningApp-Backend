from dataclasses import field, fields
from rest_framework import serializers
from .models import (Course, Quiz, Question, QuizAttempt, PDF, 
                    VideoLecture, CourseReview, Module, Instructor, 
                    CourseEnrollment, PDFSeen, VideoWatched)

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'quiz_title', 'total_marks', 'attempted_by']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'marks_obtained']

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ['id', 'title', 'pdf_file', 'read_by']

class VideoLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = ['id', 'title', 'video_file', 'watched_by']

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ['id', 'user', 'description']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'profession', 'photo', 'description']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'cover_photo', 'learning', 'skills', 'students']

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = ['id', 'user', 'course']

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'marks_obtained']

class PDFSeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFSeen
        fields = ['id', 'user', 'pdf']

class VideoWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWatched
        fields = ['id', 'user', 'video']
