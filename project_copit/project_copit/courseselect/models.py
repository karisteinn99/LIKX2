from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=63)
    ects = models.IntegerField()

    def get_prerequisite(self):
        all_objects = CourseHasPrerequisite.objects.filter(fromid_id=self.id)
        print(all_objects.values())
        prereq_list = []
        for obj in all_objects.values():
            print(obj['toid_id'])
            prereq_list.append(obj['toid_id'])
        prereq = {id:prereq_list}
        return prereq_list

    def ehv(self):
        return "hallo"

    def __str__(self):
        return self.name

class CourseHasPrerequisite(models.Model):
    fromid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id1') #foreign key CourseIDa
    toid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id2') #foreign key CourseID


    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseid = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.IntegerField()

    def __str__(self):
        return self.name


        