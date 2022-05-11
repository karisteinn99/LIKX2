
from django.db import models
from django.http import QueryDict
from .models import Course, CourseHasLabel, CourseHasPrerequisite, HeadRequirements, Semesters, SubRequirements


def check_head_requirements(selection_objects):
    '''For each HeadRequirement id, goes to SubRequirements, finds corresponding quantity and label_id, 
        gets course_id's (or objects) from CourseHasLabel (with label_id),
        then compare ects or objects
        Returns dictionary with results for every headreq and subreq{headreqid:{subreqid:True/False,subreqid:True/False},headreqid:{...}}'''
    result_dict = {}
    for semester,courses in selection_objects.items():
        for head_requirement in HeadRequirements.objects.all():
            result_dict[head_requirement] = {} 
            for sub_requirement in SubRequirements.objects.all():
                if head_requirement.id == sub_requirement.head_req_id_id:
                    labeled_queryset = sub_requirement.get_courses_with_label() #returns Course objects
                    labeled_id_list = labeled_queryset.values_list('id') #listi af idum i labeled queryset
                    labeled_selection = courses.filter(pk__in = labeled_id_list) #filtera selectionið með labelinu skila Course objects
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
    return result_dict


def count_ects(objects):
    count = 0
    for course in objects:
        count += course.ects
    return count



def change_dictionary(dict):
    old_object = Course.objects.none()
    ret_dict = {}
    #dict.pop('csrfmiddlewaretoken')
    counter = 1
    for semester,courses in dict.items():
        if semester == 'csrfmiddlewaretoken':
            continue
        else:
            if len(courses.split()) > 0:
                for course_id in courses.split():
                    course_object = Course.objects.filter(id = course_id)
                    new_queryset = course_object | old_object
                    old_object = new_queryset
                    #object_list.append(course_object)
                ret_dict[counter] =  new_queryset
                counter += 1
                old_object = Course.objects.none()
    return ret_dict



def check_prerequisite_by_semester(selected_courses_by_semester): 
    '''Fer í hverja önn og athugar hvort undanfaraskilyrðin séu í lagi fyrir annirnar á undan, fyrir hvern áfanga'''
    ret_list = []
    for semester in selected_courses_by_semester.keys():
        for course in selected_courses_by_semester[semester]:
            is_okay = True
            prereq_list = course.get_prerequisite()
            if semester == 1:
                if len(prereq_list) == 0:
                    continue
                else:
                    ret_str = "Course {} cannot be a first course, has prerequisite/s: ".format(course)
                    for prereq in prereq_list:
                        course_object = CourseHasPrerequisite.objects.get(course_id_id = course.id, prereq_id_id = prereq.id)
                        if course_object.parallel_enrollment == 0:
                            ret_str += "{}\n".format(prereq)
                        else:
                            ret_str += "{} (parallel enrollment allowed) ".format(prereq)
                    ret_list.append(ret_str)

            else:
                ret_str = ""
                is_okay = True
                false_list = []
                for prereq in prereq_list:
                    course_object = CourseHasPrerequisite.objects.get(course_id_id = course.id, prereq_id_id = prereq.id)
                    if course_object.parallel_enrollment == 0:
                        for counter in range(semester-1,0,-1):
                            print("ekki parallel - counter: {}, semester: {}, course: {}, prereq: {}".format(counter, semester, course, prereq))
                            if prereq not in selected_courses_by_semester[counter]:
                                is_okay = False
                        if not is_okay:
                            false_list.append(prereq)
                    else:
                        for counter in range(semester,0,-1):
                            print("parallel - counter: {}, semester: {}, course: {}, prereq: {}".format(counter, semester, course, prereq))
                            if prereq not in selected_courses_by_semester[counter]:
                                is_okay = False
                        if not is_okay:   
                            false_list.append(prereq)
                    
                if len(false_list) != 0:
                    ret_str += ("Course {} needs prerequisite/s:".format(course))
                    for prerequisite in false_list:
                        ret_str += "{}".format(prerequisite)
                    ret_list.append(ret_str)
    return ret_list





def check_correct_semester(selected_courses_by_semester):
    '''Checks for each semester in choice, if that course is taught on that semester'''
    ret_list = []
    for key in selected_courses_by_semester:
        for course in selected_courses_by_semester[key]:
            if "Haustönn" in course.semester_name[:len(course.semester_name)-4] and key%2 == 0:
                ret_list.append("{} is not taught during vorönn, it is taught during {}".format(course.name, course.semester_name[:len(course.semester_name)-5]))
            elif "Vorönn" in course.semester_name[:len(course.semester_name)-4] and key%2 != 0:
                ret_list.append("{} is not taught during haustönn, it is taught during {}".format(course.name, course.semester_name[:len(course.semester_name)-5]))
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
        #print(ret_list)
    return ret_list

def count_course_types(queryset):
    count_3 = 0
    count_12 = 0
    ret_dict = {}
    for course in queryset:
        if course.semester_type == "3V":
            count_3 += 1
        elif course.semester_type == "12V":
            count_12 += 1
    ret_dict["3V"] = count_3
    ret_dict["12V"] = count_12
    #print(ret_dict)
    return ret_dict