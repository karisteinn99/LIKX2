
from django.db import models
from .models import Course
from .models import CourseHasPrerequisite

def count_ects(selected_courses):
    print('inní count_ects')
    print(selected_courses)
    count = 0
    for course in selected_courses:
        count += course.ects 
        # print(count)
    if count >= 180:
        return "Success with {} ECTS of 180".format(count)
    else:
        return "Total ECTS requirement not fulfilled with {} ECTS ({} ECTS missing)".format(count, 180-count)


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


def check_prereq_by_semester(selected_courses_by_semester): # grf dict = {önn1:queryset, önn2:queryset, önn3:queryset...}
    for semester in selected_courses_by_semester.keys():
        for course in selected_courses_by_semester[semester]:
            prereq_queryset = course.get_prerequisite()
            for prereq in prereq_queryset:
                if semester==1:
                    pass
                elif prereq not in selected_courses_by_semester[semester-1]:
                    is_okay = False

                    #
                

    #fara fyrir hverja önn í values og fá undanfara, athuga í annir með lægri tölu en i, hvort prereq áfanginn sé þar

    return "hmm"

def check_correct_semester(selected_courses):
    for course in selected_courses:
        ''
    return ''