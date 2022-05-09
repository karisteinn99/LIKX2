from fnmatch import fnmatch
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import count_ects, check_head_requirements
from .models import Course, HeadRequirements, SubRequirements, CourseHasLabel, CourseHasPrerequisite, CourseSemester, Semesters

# form test og course selection smiðað saman
def course_selection(request):
    data = request.POST.items()
    name_dict = {}
    for name in data:
        name_dict[name[0]] = name[1]
    # name_dict.pop('csrfmiddlewaretoken')
    print(name_dict)

    course_objects = Course.objects.all()
    context = {'courses': course_objects}
    return render(request, 'course-selection.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')


def big_check(request):
    other_requirements_result_dict = {}
    selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    head_requirements_result_dict = check_head_requirements(selection_objects)
    # other_requirements_result_dict["prerequisite check"] = check_prerequisite_by_semester(selection_objects) #ÞEGAR GET FENGIÐ SKIPT EFTIR ÖNNUM
    # other_requirements_result_dict["type check"] = check_course_types(selection_objects) #hvort það sé rétt magn af 12V og 3V
    # other_requirements_result_dict["semester check"] = check_correct_semester(selection_objects) #hvort áfangar séu kenndir á völdu önnunum
    # context = {'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict}
    context = {'head_requirements': head_requirements_result_dict}
    return render(request,'check-test.html',context)

    
