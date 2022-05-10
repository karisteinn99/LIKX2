from fnmatch import fnmatch
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import check_head_requirements, change_dictionary, check_prerequisite_by_semester, check_correct_semester, check_course_types
from .models import Course

# form test og course selection smiðað saman
def course_selection(request):
    data = request.POST.items()
    #print(data)
    semester_dict = {}
    semester_dict_output = {}
    courses_in_calender = []
    for semester in data:
        semester_dict[semester[0]] = semester[1]
    print(semester_dict)
    # semester_dict.pop('csrfmiddlewaretoken') #virkar ekkiiiii
    #print(semester_dict)
    for semester in semester_dict.keys():
        courses_str = semester_dict[semester].split(' ')
        courses_int = []
        for course in courses_str:
            if course.isdigit():
                courses_in_calender.append(int(course))
                courses_int.append(int(course))
        semester_dict_output[semester] = courses_int        

    semester_dict = change_dictionary(semester_dict)
    check_correct_semester(semester_dict)
    check_course_types(semester_dict)
    
    head_requirements_result_dict, other_requirements_result_dict = big_check(semester_dict)
    course_objects = Course.objects.all()
    context = {'courses': course_objects, 'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict, 'semesters': semester_dict_output, 'courses_in_calender': courses_in_calender}
    #print(context)

    return render(request, 'course-selection.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')


def big_check(selected_objects_by_semester):
    other_requirements_result_dict = {}
    head_requirements_result_dict = check_head_requirements(selected_objects_by_semester)
    other_requirements_result_dict["prerequisite check"] = check_prerequisite_by_semester(selected_objects_by_semester) #ÞEGAR GET FENGIÐ SKIPT EFTIR ÖNNUM
    other_requirements_result_dict["type check"] = check_course_types(selected_objects_by_semester) #hvort það sé rétt magn af 12V og 3V
    other_requirements_result_dict["semester check"] = check_correct_semester(selected_objects_by_semester) #hvort áfangar séu kenndir á völdu önnunum
    #context = {'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict}
    # context = {'head_requirements': head_requirements_result_dict}
    # return render(request,'check-test.html',context)
    return head_requirements_result_dict, other_requirements_result_dict

    
