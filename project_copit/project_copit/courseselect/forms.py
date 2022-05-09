from dataclasses import fields
from unicodedata import name
from django.forms import ModelForm
from .models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        