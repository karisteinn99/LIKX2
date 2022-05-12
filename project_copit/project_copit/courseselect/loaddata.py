from numpy import empty
import pandas as pd
from courseselect.models import Course, CourseHasPrerequisite

tmp_data=pd.read_csv('course_info.csv',sep=';')

courses = [
    Course(
        course_code = tmp_data.loc[row-1]['CourseCode'], 
        name = tmp_data.loc[row-1]['Name'], 
        department_name = tmp_data.loc[row-1]['DepartmentName'], 
        semester_name = tmp_data.loc[row-1]['SemesterName'], 
        semester_type = tmp_data.loc[row-1]['SemesterType'],
        ects = tmp_data.loc[row-1]['ECTS'],
        description = tmp_data.loc[row-1]['Description'],
        teaching_language = tmp_data.loc[row-1]['TeachingLanguage'],
        has_prerequisite = tmp_data.loc[row-1]['Prerequisite'],
    )
    for row in tmp_data['id']
]
Course.objects.bulk_create(courses)

tmp_prereq_data=pd.read_csv('prerequisite_info.csv',sep=';')
prereq = [
    CourseHasPrerequisite(
        parallel_enrollment = tmp_prereq_data.loc[row-1]['ParallelEnrollment'],
        course_id = Course.objects.filter(course_code = tmp_prereq_data.loc[row-1]['CourseCode'])[0],
        prereq_id = Course.objects.filter(course_code = tmp_prereq_data.loc[row-1]['Prerequisite'])[0],
    )
    for row in tmp_prereq_data['id']
]
CourseHasPrerequisite.objects.bulk_create(prereq)

c1 = CourseHasPrerequisite(
    parallel_enrollment = 0,
    course_id = Course.objects.filter(course_code='T-201-GAG1'),
    prereq_id = Course.objects.filter(course_code = 'T-201-FOR1'),
)


tmp_prereq_data=pd.read_csv('prerequisite_info.csv',sep=';')
prereq_list=[]
for row in tmp_prereq_data['id']:
    course_codeinn = tmp_prereq_data.loc[row-1]['CourseCode']
    prereq_codeinn = tmp_prereq_data.loc[row-1]['Prerequisite']
    course_object = Course.objects.filter(course_code = course_codeinn)[0]
    prereq_object = Course.objects.filter(course_code = prereq_codeinn)[0]

    undanfara_objectinn = CourseHasPrerequisite(course_id=course_object, prereq_id=prereq_object,parallel_enrollment=tmp_prereq_data.loc[row-1]['ParallelEnrollment'])

    prereq_list.append(undanfara_objectinn)
CourseHasPrerequisite.objects.bulk_create(prereq_list)


    

# courses = []
# for i, row in tmp_data.iterrows():
#     courses.append(Course(
#         course_code = row['CourseCode'], 
#         name = [row]['Name'], 
#         department_name = [row]['DepartmentName'], 
#         semester_name = [row]['SemesterName'], 
  #      semester_type = [row]['SemesterType'],
 #       ects = [row]['ECTS'],
#        description = [row]['Description'],
#        teaching_language = [row]['TeachingLanguage'],
#        has_prerequisite = [row]['Prerequisite'],
#    ))

#Course.objects.bulk_create(courses)