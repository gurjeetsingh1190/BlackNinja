from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Application(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rank = models.IntegerField(null=True, blank=True)


