
from select import select

def count_etcs(selected_courses):
    count_etc = 0
    for course in selected_courses:
        count_etc += select_course[course].etcs[4] # breyta tölunni 4 í staksnúmerið á etc í dictinu sem er skilað 
    if count_etc >= 180:
        return (True, count_etc)
    else:
        return (False, count_etc)

def check_success_etcs(ret_tup):
    if ret_tup[1] == True:
        result_string = ''