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
        all_objects = CourseHasPrerequisite.objects.raw("select * from CourseHasPrerequisite where fromid_id=7")
        for obj in all_objects:
            print(obj)
        prereq_list = all_objects.toid_id
        
#        for object in all_objects:
#            prereq_list = []
#            prereq_list.append(all_objects.toid_id)
        return prereq_list

    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseid = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.IntegerField()

    def __str__(self):
        return self.name


        