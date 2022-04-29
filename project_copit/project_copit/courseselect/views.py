from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import CourseHasPrerequisite
from .models import CourseSemester



def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def course_selection(request):
    course_objects = Course.objects.all()
    for c in course_objects:
        print(c)
    context = {'courses':course_objects}
    return render(request, 'course-selection.html',context)

def courses_by_semester(request): #þetta má vera filter bara
    c = Course.objects.all()
    context = {'data': c}
    return render(request, 'semester-test.html',context)

    #course_objects = CourseSemester.objects.raw("select * from courseselect_course C join courseselect_coursesemester S on S.courseid_id = C.ID where S.semesterid=1")

    
