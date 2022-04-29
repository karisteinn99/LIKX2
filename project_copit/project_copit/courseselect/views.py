from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import count_ects
from .models import Course
from .models import CourseHasPrerequisite
from .models import CourseSemester

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')

def course_selection(request):
    course_objects = Course.objects.all()
    context = {'courses':course_objects}
    return render(request, 'course-selection.html',context)


    #course_objects = CourseSemester.objects.raw("select * from courseselect_course C join courseselect_coursesemester S on S.courseid_id = C.ID where S.semesterid=1")

def big_check(request):
    course_objects = Course.objects.all() #þetta verður væntanlega valið hjá user
    
    ects_req = check_ects_requirements(course_objects) #check ects
    context = {'ects_req': ects_req}

    #fleiri check



    return render(request, 'course-selection.html', context)

def check_ects_requirements(course_objects):
    return count_ects(course_objects)
    
