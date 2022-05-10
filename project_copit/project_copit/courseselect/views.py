from fnmatch import fnmatch
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import check_head_requirements, change_dictionary, check_correct_semester, check_course_types, check_prerequisite_by_semester
from .models import Course, HeadRequirements, SubRequirements, CourseHasLabel, CourseHasPrerequisite, CourseSemester, Semesters

# form test og course selection smiðað saman
def course_selection(request):
    data = request.POST.items()
    #print(data)
    name_dict = {}
    for semester in data:
        name_dict[semester[0]] = semester[1]
    print(name_dict)
    # name_dict.pop('csrfmiddlewaretoken') #virkar ekkiiiii
    #print(name_dict)
    name_dict = change_dictionary(name_dict)
    check_correct_semester(name_dict)
    check_course_types(name_dict)
    
    head_requirements_result_dict, other_requirements_result_dict = big_check(name_dict)
    course_objects = Course.objects.all()
    context = {'courses': course_objects, 'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict}
    #print(context)
    return render(request, 'course-selection.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')


def big_check(selected_objects_by_semester):
    other_requirements_result_dict = {}
    total_selected_objects = Course.objects.none()
    for semester, queryset in sorted(selected_objects_by_semester.items(), reverse=True):
        total_selected_objects.union(queryset) #mögulega ekki hægt að filtera union
    #selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    head_requirements_result_dict = check_head_requirements(total_selected_objects)
    other_requirements_result_dict["prerequisite check"] = check_prerequisite_by_semester(selected_objects_by_semester) #ÞEGAR GET FENGIÐ SKIPT EFTIR ÖNNUM
    other_requirements_result_dict["type check"] = check_course_types(selected_objects_by_semester) #hvort það sé rétt magn af 12V og 3V
    other_requirements_result_dict["semester check"] = check_correct_semester(selected_objects_by_semester) #hvort áfangar séu kenndir á völdu önnunum
    #context = {'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict}
    # context = {'head_requirements': head_requirements_result_dict}
    # return render(request,'check-test.html',context)
    return head_requirements_result_dict, other_requirements_result_dict

    
