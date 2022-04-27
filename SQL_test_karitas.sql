------------- SKOÐA TÖFLUR:
select * -- sjá allar joinaðar í eina töflu
from courseselect_coursehasprerequisite P
join courseselect_course C on C.ID = P.ID
join courseselect_coursesemester S on P.ID = S.ID

select * from courseselect_course -- sjá course töfluna
select * from courseselect_coursehasprerequisite -- sjá coursehasprerequisite töfluna
select * from courseselect_coursesemester -- sjá coursesemester töfluna

select C.ID from courseselect_course C where C.name = 'Stærðfræði II'
select C.name from courseselect_course C where C.ID = 2


-------------- DELETE:
DELETE FROM courseselect_course C WHERE C.ID = 6 -- delete-a instönsum

-------------- INSERT:
-- Course
INSERT INTO courseselect_course(ID,name, ects) values(1,'Stærðfræði I', 6)
INSERT INTO courseselect_course(name, ects) values('Stærðfræði II', 6)
INSERT INTO courseselect_course(name, ects) values('Línuleg algebra', 6)

-- CourseHasPrerequisite
INSERT INTO courseselect_coursehasprerequisite(fromID_id, toID_id) values(5,6) -- fæ villu hér að þessir dálkar séu ekki til
INSERT INTO courseselect_coursehasprerequisite(fromID_id, toID_id) values('5','4')

-- CourseSemester
INSERT INTO courseselect_coursesemester(semesterID, courseID_id) VALUES(1,7)
INSERT INTO courseselect_coursesemester(semesterID, courseID_id) VALUES(2,7)

