from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import CourseHasPrerequisite
from .models import CourseSemester


def homepage(request):
    course_list = Course.objects.all()
    output = ",".join([course.name for course in course_list])
    return HttpResponse(output)