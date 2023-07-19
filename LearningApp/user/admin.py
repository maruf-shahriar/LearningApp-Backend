from django.contrib import admin
from .models import CustomUser, EnrolledCourse
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(EnrolledCourse)
