from django.contrib import admin
from .models import Course, Quiz, PDF, VideoLecture, CourseReview, Question, Module, Instructor, CourseEnrollment
# Register your models here.
admin.site.register((Course, Quiz, PDF, VideoLecture, CourseReview, Question, Module, Instructor, CourseEnrollment))