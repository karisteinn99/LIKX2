from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import CourseHasPrerequisite
from .models import CourseSemester


def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def course_selection(request):
    course_list = Course.objects.all()
    output = ",".join([course.name for course in course_list])
    test_list = [1,2,3,4,5,6]
    context = {'data':output,'list':test_list}
    return render(request, 'course-selection.html',context)
