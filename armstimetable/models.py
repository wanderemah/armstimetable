from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username


class Lecturer(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    profile = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=15)

    # image = models.ImageField()
    # cv = models.FileField()

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255, unique=False, blank=True)

    def __str__(self):
        return self.specialty


class allowedCourse(models.Model):
    degree = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return self.degree


class Student(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    course = models.ForeignKey(allowedCourse, on_delete=models.CASCADE)
    profile = models.TextField()

    # image = models.ImageField()
    # cv = models.FileField()

    def __str__(self):
        return self.name


class Event(models.Model):
    tutor = models.ForeignKey(Lecturer, on_delete=models.CASCADE, unique=False)
    topic = models.CharField(max_length=255, primary_key=True, unique=True)
    description = models.TextField()
    date = models.DateTimeField(unique=False)
    venue = models.CharField(max_length=20, default='Room 170')
    complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('timetable:docket')

    def __str__(self):
        return self.topic

class References(models.Model):
    field = models.ForeignKey(Event,on_delete=models.CASCADE)
    reference = models.CharField(max_length=255)


class Comment(models.Model):
    topic = models.ForeignKey(Event, unique=False, on_delete=models.CASCADE)
    student = models.CharField(max_length=30)
    query = models.TextField(primary_key=True, max_length=255, unique=False)

    def __str__(self):
        return self.query


class Responses(models.Model):
    query = models.ForeignKey(Comment, on_delete=models.CASCADE)
    tutor = models.CharField(max_length=25, blank=True)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.answer
