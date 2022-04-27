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
    course_list = ",".join([course.name for course in course_objects])
    test_list = [1,2,3,4,5,6]
    context = {'data':course_list,'list':test_list}
    return render(request, 'course-selection.html',context)

def courses_by_semester(request):
    course_objects = CourseSemester.objects.raw("select * from courseselect_course C join courseselect_coursesemester S on S.courseid_id = C.ID where S.semesterid=3")
    course_list = ",".join([str(course.name) for course in course_objects])
    context = {'data': course_list}
    return render(request, 'semester-test.html',context)
    
