from rest_framework import serializers
from .models import Course, Quiz, PDF, VideoLecture, CourseReview, EnrolledStudent

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

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
    quizzes = QuizSerializer(many=True, read_only=True)
    pdfs = PDFSerializer(many=True, read_only=True)
    video_lectures = VideoLectureSerializer(many=True, read_only=True)
    reviews = CourseReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'quizzes', 'pdfs', 'video_lectures', 'reviews']

class EnrolledStudentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = EnrolledStudent
        fields = ['id', 'course', 'course_title', 'user', 'user_email']
