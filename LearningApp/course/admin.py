from django.contrib import admin
from .models import Course, Quiz, PDF, VideoLecture, CourseReview, Question, EnrolledStudent
# Register your models here.
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(PDF)
admin.site.register(VideoLecture)
admin.site.register(CourseReview)
admin.site.register(EnrolledStudent)
