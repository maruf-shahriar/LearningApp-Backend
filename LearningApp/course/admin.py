from django.contrib import admin
from .models import Course, Quiz, PDF, VideoLecture, CourseReview, Question, Module, Instructor, CourseEnrollment, QuizAttempt
# Register your models here.
admin.site.register((Course, CourseEnrollment, Module, Instructor, CourseReview, Quiz, QuizAttempt, Question, PDF, VideoLecture))