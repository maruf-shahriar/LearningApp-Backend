from django.db import models
from django.contrib.auth import get_user_model

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
    learning = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.title

class Instructor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='course/instructor', blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.name}"

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.course.title} - {self.name}"


class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    quiz_title = models.TextField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.module.course.title} - {self.module.name} - {self.quiz_title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(null=True)

    def __str__(self):
        return self.question

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.quiz.quiz_title}"

class PDF(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='course/pdfs/')

    def __str__(self):
        return f"- {self.module.course.title} - {self.module.name} - {self.title}"

class VideoLecture(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='course/videos/')

    def __str__(self):
        return f"- {self.module.course.title} - {self.module.name} - {self.title}"

class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - Review"

class EnrolledStudent(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='enrolled_students')
    email = models.EmailField()

    def __str__(self):
        return self.email