from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from courseselect.checks import count_ects, check_prereq
from courseselect.checks import check_prereq_by_semester
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
    '''For each HeadRequirement id, goes to SubRequirements, finds corresponding quantity and label_id, 
        gets course_id's (or objects) from CourseHasLabel (with label_id),
        counts ects of '''
    result_dict = {} 
    selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    for head_requirement in HeadRequirements.objects.all():
        print("Head requirement:{}".format(head_requirement))
        for sub_requirement in SubRequirements.objects.all():
            print("Sub requirement:{}".format(sub_requirement))
            if head_requirement.id == sub_requirement.head_req_id_id:
                labeled_queryset = sub_requirement.get_courses_with_label() #returns Course objects
                print(labeled_queryset)
                labeled_id_list = labeled_queryset.values_list('id') #listi af idum i labeled queryset
                labeled_selection = selection_objects.filter(pk__in = labeled_id_list) #filtera selectionið með labelinu skila Course objects ÞARF AÐ LAGA
                if sub_requirement.quantity == -1: #selectionið þarf að innihalda öll objects sem finnast með þessu labeli
                    if labeled_selection.union(labeled_queryset) == labeled_selection:
                        result_dict[head_requirement.id][sub_requirement.id]=True
                    else:
                        result_dict[head_requirement.id][sub_requirement.id]=False
                else: #bera saman selection og labeled queryset einingarnar mv quantity
                    if labeled_selection.count_ects >= sub_requirement.quantity: #fulfils this sub requirement
                        result_dict[head_requirement.id][sub_requirement.id]=True
                    else:
                        result_dict[head_requirement.id][sub_requirement.id]=False
    #result_dict = {1:{1:True,2:False,3:True},2:{1:False, 2:True, 3:True}...}
    return result_dict
#######TESTA#######í terminal:
from courseselect.models import Course, HeadRequirements, SubRequirements, CourseHasLabel, CourseHasPrerequisite, CourseSemester, Semesters
from courseselect.checks import count_ects, check_prereq
result_dict = {} 
selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
for head_requirement in HeadRequirements.objects.all():
    print("Head requirement:{}".format(head_requirement))
    for sub_requirement in SubRequirements.objects.all():
        print("Sub requirement:{}".format(sub_requirement))
        if head_requirement.id == sub_requirement.head_req_id_id:
            print("inní if1") #kemst hingað
            labeled_queryset = sub_requirement.get_courses_with_label() #returns Course objects FÖST HÉR
            print(labeled_queryset)
            labeled_id_list = labeled_queryset.values_list('id') #listi af idum i labeled queryset
            labeled_selection = selection_objects.filter(pk__in = labeled_id_list) #filtera selectionið með labelinu skila Course objects ÞARF AÐ LAGA
            if sub_requirement.quantity == -1: #selectionið þarf að innihalda öll objects sem finnast með þessu labeli
                print("inní if2")
                if labeled_selection.union(labeled_queryset) == labeled_selection:
                    result_dict[head_requirement.id][sub_requirement.id]=True
                else:
                    result_dict[head_requirement.id][sub_requirement.id]=False
            else: #bera saman selection og labeled queryset einingarnar mv quantity
                if labeled_selection.count_ects >= sub_requirement.quantity: #fulfils this sub requirement
                    result_dict[head_requirement.id][sub_requirement.id]=True
                else:
                    result_dict[head_requirement.id][sub_requirement.id]=False
print(result_dict)

    # check_result_dict = {} #{heareq_id:'result',...}
    # course_objects = Course.objects.all() #þetta verður væntanlega valið hjá user - BREYTA Í DICT
    # #print(course_objects)
    # check_result_list.append(check_head_requirements())

    # check_result_list.append(check_ects_requirements(course_objects)) #check ects
    # #print(check_result_list)
    # check_result_list.append(check_prereq_requirements(course_objects)) #prerequisites

    # context = {'big_req':check_result_list}
    # print(context)
    # return render(request, 'check-test.html', context)


def check_ects_requirements(course_objects):
    '''hér gætu fleiri eininga tjékk verið t.d. kröfurnar, kalla í checks.py'''
    return count_ects(course_objects)

def check_prereq_requirements(course_objects):
    return check_prereq_by_semester(course_objects)
    
