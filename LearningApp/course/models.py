from django.db import models
from django.contrib.auth import get_user_model
from user.models import CustomUser

User = get_user_model()

# Create your models here.
class Course(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    CATEGORY_CHOICES = (
        ('Database', 'db'),
        ('Programming', 'coding'),
        ('Software Engineering', 'swe'),
        ('ML', 'ml'),
        ('UI/UX', 'ui/ux'),
    )
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    cover_photo = models.ImageField(upload_to='course/cover', blank=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

class PDF(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='course/pdfs/')

class VideoLecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='course/videos/')

class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class EnrolledStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')