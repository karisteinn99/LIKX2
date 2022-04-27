select *
from courseselect_coursehasprerequisite P
join courseselect_course C on C.ID = P.ID
join courseselect_coursesemester S on P.ID = S.ID

select C.ID from courseselect_course C where C.name = 'Stærðfræði I'


-- Course
INSERT INTO courseselect_course(name, ects) values('Stærðfræði I', 6)
INSERT INTO courseselect_course(name, ects) values('Stærðfræði II', 6)
INSERT INTO courseselect_course(name, ects) values('Línuleg algebra', 6)

-- CourseHasPrerequisite
INSERT INTO courseselect_coursehasprerequisite(fromID_id, toID_id) values('5','6')
INSERT INTO courseselect_coursehasprerequisite(fromID, toID) values('5','4')


-- CourseSemester

