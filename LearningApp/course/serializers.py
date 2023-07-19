from rest_framework import serializers
from .models import Course, Quiz, Question, QuizAttempt, PDF, VideoLecture, CourseReview, EnrolledStudent

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'quiz_title', 'total_marks']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_answer', 'is_correct']

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'marks_obtained']

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ['id', 'title', 'pdf_file']

class VideoLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = ['id', 'title', 'video_file']

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ['id', 'user', 'description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructor', 'cover_photo']

class EnrolledStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledStudent
        fields = ['id', 'email']
