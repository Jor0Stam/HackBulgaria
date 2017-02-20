from django.forms import ModelForm
from django import forms as some_form
from .models import Course


class EditCourse(ModelForm):
    class Meta:
        model = Course
        fields = ['name',
                  'description',
                  'start_date',
                  'end_date']
