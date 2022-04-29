
from django.db import models
from .models import Course
from .models import CourseHasPrerequisite

def count_ects(selected_courses):
    print('inní count_ects')
    print(selected_courses)
    count = 0
    for course in selected_courses:
        count += course.ects 
        print(count)
    if count >= 180:
        return "Success with % ECTS of 180".format(count)
    else:
        return "ECTS requirement not fulfilled with % ECTS (% ECTS missing)".format(count, 180-count)

#def check_success_etcs(ret_tup):
#    if ret_tup[0] == True:
#        return 'Success with % ECTS'.format(ret_tup[1])
#    else:
#        return 'ECTS requirement not fulfilled with % ECTS (% ECTS missing)'.format(ret_tup[1],180-ret_tup[1])


def check_prereq(selected_courses): #bara dæmi um object sem eru valin
    prereq_list = []
    is_okay = True
    false_list = []
    for course in selected_courses:
        prereq_list.append(course.get_prerequisite) #prereqs fyrir þennan course
        for prereq in prereq_list:
            print(prereq)#leita að id-inu af prereq í selected courses

            #ef id finnst ekki: is_okay = False og false_list.append(prereq)
    # if is_okay = True: ret_str = 'Prerequisites okay!'
    # else: ret_str 'Prerequisites not okay! Missing courses are: %'.format(false_list) gera lika fromid hliðiná toid
    return 'bla' #ret_str


