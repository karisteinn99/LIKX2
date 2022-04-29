
from .models import CourseHasPrerequisite
from .models import Course

def count_etcs(selected_courses):
    count = 0
    for course in selected_courses:
        count += selected_courses[course].ects[4] # breyta tölunni 4 í staksnúmerið á etc í dictinu sem er skilað 
    if count >= 180:
        return (True, count)
    else:
        return (False, count)

def check_success_etcs(ret_tup):
    if ret_tup[0] == True:
        return 'Success'
    else:
        return 'ECTS requirement not fulfilled % ECTS missing'.format(180-ret_tup[1])


def check_prereq(selected_courses=[{'id': 7, 'name': 'Stærðfræði II', 'ects': 6}, {'id': 8, 'name': 'Línuleg algebra', 'ects': 6}]):
    for course in selected_courses:
        prereq_list = get_prerequisite(course['id'])
        

