from fnmatch import fnmatch
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import check_head_requirements, change_dictionary, check_prerequisite_by_semester, check_correct_semester, check_course_types, check_ects_per_semester
from .models import Course, SubRequirements, Label

# form test og course selection smiðað saman
def course_selection(request):
    data = request.POST.items()
    semester_dict = {}
    semester_dict_output = {}
    courses_in_calender = []
    for semester in data:
        semester_dict[semester[0]] = semester[1]
    for semester in semester_dict.keys():
        courses_str = semester_dict[semester].split(' ')
        courses_int = []
        for course in courses_str:
            if course.isdigit():
                courses_in_calender.append(int(course))
                courses_int.append(int(course))
        semester_dict_output[semester] = courses_int        

    semester_dict = change_dictionary(semester_dict)
    head_requirements_result_dict, other_requirements_result_dict = big_check(semester_dict)
    course_objects = Course.objects.all()

    label_objects = Label.objects.all()
    label_dict = {}
    for label in label_objects:
        label_dict[label] = label.get_courses_with_label
    context = {'courses': course_objects, 'head_requirements': head_requirements_result_dict, 'other_requirements': other_requirements_result_dict, 'semesters': semester_dict_output, 'courses_in_calender': courses_in_calender, 'label_dict': label_dict}
    return render(request, 'course-selection.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def homepage(request):
    return render(request, 'homepage.html')


def big_check(selected_objects_by_semester):
    other_requirements_result_dict = {}
    head_requirements_result_dict = check_head_requirements(selected_objects_by_semester)
    other_requirements_result_dict["prerequisite errors"] = check_prerequisite_by_semester(selected_objects_by_semester) #ÞEGAR GET FENGIÐ SKIPT EFTIR ÖNNUM
    other_requirements_result_dict["semester errors"] = check_correct_semester(selected_objects_by_semester) #hvort áfangar séu kenndir á völdu önnunum
    other_requirements_result_dict[" "] = check_course_types(selected_objects_by_semester) #hvort það sé rétt magn af 12V og 3V
    other_requirements_result_dict["  "] = check_ects_per_semester(selected_objects_by_semester)
    return head_requirements_result_dict, other_requirements_result_dict

    
