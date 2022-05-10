
from django.db import models
from django.http import QueryDict
from .models import Course, CourseHasLabel, CourseHasPrerequisite, HeadRequirements, Semesters, SubRequirements


def check_head_requirements(selection_objects):
    '''For each HeadRequirement id, goes to SubRequirements, finds corresponding quantity and label_id, 
        gets course_id's (or objects) from CourseHasLabel (with label_id),
        then compare ects or objects
        Returns dictionary with results for every headreq and subreq{headreqid:{subreqid:True/False,subreqid:True/False},headreqid:{...}}'''
    result_dict = {}
    #selection_objects = Course.objects.all() #BREYTA SVO Í ACTUAL USER INPUTTIÐ
    for head_requirement in HeadRequirements.objects.all():
        result_dict[head_requirement] = {} 
        for sub_requirement in SubRequirements.objects.all():
            if head_requirement.id == sub_requirement.head_req_id_id:
                labeled_queryset = sub_requirement.get_courses_with_label() #returns Course objects
                labeled_id_list = labeled_queryset.values_list('id') #listi af idum i labeled queryset
                labeled_selection = selection_objects.filter(pk__in = labeled_id_list) #filtera selectionið með labelinu skila Course objects
                if sub_requirement.quantity == -1: #selectionið þarf að innihalda öll objects sem finnast með þessu labeli
                    if labeled_selection.union(labeled_queryset) == labeled_selection:
                        result_dict[head_requirement][sub_requirement]="Fulfilled" 
                    else:
                        result_dict[head_requirement][sub_requirement]="Not fulfilled"
                else: #bera saman selection og labeled queryset einingarnar mv quantity
                    if count_ects(labeled_selection) >= sub_requirement.quantity: #fulfils this sub requirement
                        result_dict[head_requirement][sub_requirement]="Fulfilled"
                    else:
                        result_dict[head_requirement][sub_requirement]="Not fulfilled"
    print(result_dict)
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

def change_dictionary(dict):
    ret_dict = {}
    #dict.pop('csrfmiddlewaretoken')
    for semester,courses in dict.items():
        if semester == 'csrfmiddlewaretoken':
            continue
        else:
            old_object = Course.objects.none()
            for course_id in courses.split():
                course_object = Course.objects.filter(id = course_id)
                new_queryset = course_object.union(old_object)
                old_object = new_queryset
                #object_list.append(course_object)
                ret_dict[semester] =  new_queryset
    print(ret_dict)
    return ret_dict



def check_prerequisite_by_semester(selected_courses_by_semester): # grf dict = {önn1:queryset, önn2:queryset, önn3:queryset...}
    '''Fer í hverja önn og athugar hvort undanfaraskilyrðin séu í lagi fyrir annirnar á undan, fyrir hvern áfanga'''
    print('inní check_prereq_by_semester')
    print(selected_courses_by_semester.keys())
    ret_list = []
    for semester in selected_courses_by_semester.keys():
        print(semester)
        is_okay = True
        for course in selected_courses_by_semester[semester]:
            print(course)
            prereq_list = course.get_prerequisite()
            if semester == "Haustönn 1":
                if len(prereq_list) == 0:
                    continue
                else:
                    for prereq in prereq_list:
                        ret_list.append("Course {} has prerequisite {}".format(course, prereq))
            else:
                for prereq in prereq_list:
                    print("prereq: {}".format(prereq))
                    #bæta við parallel
                    for counter in range(len(selected_courses_by_semester.keys()),2):
                        print("counter: {}".format(counter))
                        is_okay = True
                        if prereq not in selected_courses_by_semester[counter-1]:
                            is_okay = False
                            #missing_list.append(prereq.course_code)
                    if is_okay==False:
                        ret_list.append("Semester {} missing {} because of {} on semester {}\n".format(counter, prereq, course, semester))
    print(ret_list)
    return ret_list



def check_correct_semester(selected_courses_by_semester):
    '''Checks for each semester in choice, if that course is taught on that semester'''
    ret_list = []
    for key in selected_courses_by_semester:
        print(key[:len(key)-1])
        for course in selected_courses_by_semester[key]:
            print(course)
            if "Haustönn" in course.semester_name[:len(course.semester_name)-4] and "Haustönn" not in key[:len(key)-1]:
                ret_list.append("{} not taught during {}, it is taught during {}".format(course.name, key[:len(key)-2], course.semester_name[:len(course.semester_name)-5]))
            elif "Vorönn" in course.semester_name[:len(course.semester_name)-4] and "Vorönn" not in key[:len(key)-1]:
                ret_list.append("{} not taught during {}, it is taught during {}".format(course.name, key[:len(key)-2], course.semester_name[:len(course.semester_name)-5]))
    print(ret_list)
    return ret_list



def check_course_types(selected_courses_by_semester): # grf dict = {önn1:queryset, önn2:queryset, önn3:queryset...}
    '''Checks how many 3V courses are on each semester and 12V, returns results'''
    ret_list = []
    for semester in selected_courses_by_semester:
        type_dict = count_course_types(selected_courses_by_semester[semester])
        if type_dict["3V"] > 1:
            ret_list.append("Too many 3V courses on semester {}".format(semester))
        if type_dict["12V"] > 5:
            ret_list.append("Too many 12V courses on semester {}".format(semester))
        print(ret_list)
    return ret_list

def count_course_types(queryset):
    count_3 = 0
    count_12 = 0
    ret_dict = {}
    for course in queryset:
        if course.semester_type == "3V":
            print(course.semester_type)
            count_3 += 1
        elif course.semester_type == "12V":
            count_12 = 0
    ret_dict["3V"] = count_3
    ret_dict["12V"] = count_12
    return ret_dict