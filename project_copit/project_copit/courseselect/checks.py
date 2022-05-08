
from django.db import models
from .models import Course, CourseHasLabel, CourseHasPrerequisite, HeadRequirements, SubRequirements


def check_head_requirements(selection_objects):
    '''For each HeadRequirement id, goes to SubRequirements, finds corresponding quantity and label_id, 
        gets course_id's (or objects) from CourseHasLabel (with label_id),
        then compare ects or objects
        Returns dictionary with results for every headreq and subreq{headreqid:{subreqid:True/False,subreqid:True/False},headreqid:{...}}'''
    result_dict = {}
    selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    for head_requirement in HeadRequirements.objects.all():
        result_dict[head_requirement] ={} #
        for sub_requirement in SubRequirements.objects.all():
            if head_requirement.id == sub_requirement.head_req_id_id:
                labeled_queryset = sub_requirement.get_courses_with_label() #returns Course objects
                labeled_id_list = labeled_queryset.values_list('id') #listi af idum i labeled queryset
                labeled_selection = selection_objects.filter(pk__in = labeled_id_list) #filtera selectionið með labelinu skila Course objects
                if sub_requirement.quantity == -1: #selectionið þarf að innihalda öll objects sem finnast með þessu labeli
                    if labeled_selection.union(labeled_queryset) == labeled_selection:
                        result_dict[head_requirement][sub_requirement]="Fulfilled" #fæ villu þegar ég læt skila bara head_requirement og sub_requirement, væri betra samt
                    else:
                        result_dict[head_requirement][sub_requirement]="Not fulfilled"
                else: #bera saman selection og labeled queryset einingarnar mv quantity
                    if count_ects(labeled_selection) >= sub_requirement.quantity: #fulfils this sub requirement
                        result_dict[head_requirement][sub_requirement]="Fulfilled"
                    else:
                        result_dict[head_requirement][sub_requirement]="Not fulfilled"
    return result_dict


def count_ects(objects):
    count = 0
    for course in objects:
        count += course.ects
    return count


def check_prereq(selected_courses): #listi af objects sem eru valin(eftir önnum??) g.r.f. dictionary {önn:objects,önn:objects}
    '''Checks if prerequisites are anywhere in selected courses'''
    is_okay = True
    false_list = []
    for course in selected_courses:
        prereq_list = course.get_prerequisite() #prereqs fyrir þennan course
        for prereq in prereq_list:
            if prereq not in selected_courses:
                print("{} missing".format(prereq.course_code))
                is_okay = False
                false_list.append(prereq)
                                
    if is_okay == True:
        return "Prerequisites okay!"
    else:
        return "Prerequisites not okay! Missing courses are: {}".format(false_list) #vantar að hafa nöfnin sem output ekki objects


def check_prerequisite_by_semester(selected_courses_by_semester): # grf dict = {önn1:queryset, önn2:queryset, önn3:queryset...}
    '''Fer í hverja önn og athugar hvort undanfaraskilyrðin séu í lagi fyrir annirnar á undan, fyrir hvern áfanga'''
    print('inní check_prereq_by_semester')
    for semester in selected_courses_by_semester.keys():
        if semester == 1:
            pass
        else:
            for course in selected_courses_by_semester[semester]:
                prereq_queryset = course.get_prerequisite()
                for prereq in prereq_queryset:
                    #bæta við parallel
                    for counter in range(semester,2):
                        is_okay=True
                        if prereq not in selected_courses_by_semester[counter-1]:
                            is_okay = False
                            #missing_list.append(prereq.course_code)
                    if is_okay==False:
                        ret_str += "Semester {} missing {} because of {} on semester {}\n".format(counter, prereq, course, semester)
    return ret_str

def check_correct_semester(selected_courses):
    '''Checks for each semester in choice, if that course is taught on that semester'''
    for course in selected_courses:
        ''
    return ''