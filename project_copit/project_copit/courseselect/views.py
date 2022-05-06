from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import count_ects, check_prereq
from .models import Course
from .models import CourseHasPrerequisite
from .models import CourseSemester
from .models import Semesters

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')

def course_selection(request):
    course_objects = Course.objects.all()
    context = {'courses': course_objects}
    return render(request, 'course-selection.html',context)

def big_check(request):
    check_result_list = [] 
    course_objects = Course.objects.all() #þetta verður væntanlega valið hjá user
    print(course_objects)
    check_result_list.append(check_ects_requirements(course_objects)) #check ects
    print(check_result_list)

    check_result_list.append(check_prereq_requirements(course_objects)) #prerequisites

    #fleiri check

    context = {'big_req':check_result_list}
    print(context)
    return render(request, 'check-test.html', context)

def check_ects_requirements(course_objects):
    '''hér gætu fleiri eininga tjékk verið t.d. kröfurnar, kalla í checks.py'''
    return count_ects(course_objects)

def check_prereq_requirements(course_objects):
    return check_prereq(course_objects)
    
