import pandas as pd
from .models import Course

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



courses = []
for i, row in tmp_data.iterrows():
    courses.append(Course(
        course_code = row['CourseCode'], 
        name = [row]['Name'], 
        department_name = [row]['DepartmentName'], 
        semester_name = [row]['SemesterName'], 
        semester_type = [row]['SemesterType'],
        ects = [row]['ECTS'],
        description = [row]['Description'],
        teaching_language = [row]['TeachingLanguage'],
        has_prerequisite = [row]['Prerequisite'],
    ))

Course.objects.bulk_create(courses)