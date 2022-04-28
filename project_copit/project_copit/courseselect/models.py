from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=63)
    ects = models.IntegerField()

    def __str__(self):
        return self.name

class CourseHasPrerequisite(models.Model):
    fromid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id1') #foreign key CourseIDa
    toid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id2') #foreign key CourseID

    def get_prerequisite(courseid):
        prereq_objects = CourseHasPrerequisite.objects.raw("select * from courseselect_coursehasprerequisite where fromid_id=7")
        #for obj in all_objects:
        #    prereq_list = []
        #    prereq_list.append(obj.toid)
        return prereq_objects

    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseid = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.IntegerField()

    def __str__(self):
        return self.name


        