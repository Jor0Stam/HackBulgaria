from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
