from django.db import models
from Hack_Fmi.courses.models import Course

# Create your models here.


class Lecture(models.Model):
    name = models.CharField(max_length=200, unique=True)
    week = models.CharField(max_length=10)
    course = models.ForeignKey(Course)
    url = models.URLField(max_length=50)

    def __str__(self):
        return("Lecture - {}".format(Lecture.objects.name))

    def __repr__(self):
        return("Lecture - {}".format(Lecture.objects.name))
