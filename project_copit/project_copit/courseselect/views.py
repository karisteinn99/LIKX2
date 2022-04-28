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
    context = {'courses':course_objects}
    return render(request, 'course-selection.html',context)

def courses_by_semester(request):
    c = Course.objects.all()
    context = {'data': c}
    return render(request, 'semester-test.html',context)

def get_prerequisite(request): #kemur id-ið sem við viljum tjékka hér í request?
    prereq_objects=CourseHasPrerequisite.get_prerequisite(courseid=7)
    prereq_list = []
    for obj in prereq_objects:
        prereq_list.append(obj.toid_id)
    context = {'prereq': prereq_list}
    return render(request, 'course-selection.html',context)

    #course_objects = CourseSemester.objects.raw("select * from courseselect_course C join courseselect_coursesemester S on S.courseid_id = C.ID where S.semesterid=1")




    
