------------- SKOÐA TÖFLUR:
----áfangar,önn:
select * from courseselect_course C join courseselect_coursesemester S on (S.courseid_id) = C.ID
----áfangaID, áfanganafn, undanfara_id, undanfaranafn
select C1.ID,C1.name as course_name, P.toid_id as prerequisite_courseID, C2.name as prerequisite_course_name
from courseselect_coursehasprerequisite P
join courseselect_course C1 on C1.ID = P.fromid_id
join courseselect_course C2 on C2.ID = P.toid_id

select * from courseselect_course -- sjá course töfluna
select * from courseselect_coursehasprerequisite -- sjá coursehasprerequisite töfluna
select * from courseselect_coursesemester -- sjá coursesemester töfluna

select C.ID from courseselect_course C where C.name = 'Línuleg algebra'
select C.name from courseselect_course C where C.ID = 1


-------------- DELETE:
DELETE FROM courseselect_course C WHERE C.ID = 6 -- delete-a instönsum

-------------- INSERT:
-- Course
INSERT INTO courseselect_course(ID,name, ects) values(1,'Stærðfræði I', 6)
INSERT INTO courseselect_course(name, ects) values('Stærðfræði II', 6)
INSERT INTO courseselect_course(name, ects) values('Línuleg algebra', 6)

-- CourseHasPrerequisite
INSERT INTO courseselect_coursehasprerequisite (fromid_id, toid_id) values(7,1) 
INSERT INTO courseselect_coursehasprerequisite(fromid_id, toid_id) values(7,8)
INSERT INTO courseselect_coursehasprerequisite(fromid_id, toid_id) values(1,7)
INSERT INTO courseselect_coursehasprerequisite(fromid_id, toid_id) values(8,7)

-- CourseSemester
INSERT INTO courseselect_coursesemester(semesterid, courseid_id) VALUES(3,7) -- stæ2 um vor
INSERT INTO courseselect_coursesemester(semesterid, courseid_id) VALUES(1,1) -- stæ1 um haust
INSERT INTO courseselect_coursesemester(semesterid, courseid_id) VALUES(3,1) --stæ1 um vor
INSERT INTO courseselect_coursesemester(semesterid, courseid_id) VALUES(3,8) --lína um vor

