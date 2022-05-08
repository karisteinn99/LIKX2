from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import count_ects, check_prerequisite_by_semester, check_head_requirements
from .models import Course, HeadRequirements, SubRequirements, CourseHasLabel, CourseHasPrerequisite, CourseSemester, Semesters

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')

def course_selection(request):
    course_objects = Course.objects.all()
    context = {'courses': course_objects}
    return render(request, 'course-selection.html',context)

def big_check(request):

    selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    result_dict = check_head_requirements(selection_objects)
    #result_dict["prerequisite check"] = check_prerequisite_by_semester(selection_objects) ÞEGAR GET FENGIÐ SKIPT EFTIR ÖNNUM
    context = {'requirements': result_dict}
    return render(request,'check-test.html',context)

    
