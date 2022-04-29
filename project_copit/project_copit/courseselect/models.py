from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=63)
    ects = models.IntegerField()

    def get_prerequisite(self):
        all_objects = CourseHasPrerequisite.objects.filter(fromid_id=self.id)
        
        prereq_list = []
        for obj in all_objects.values():
            prereq_list.append(Course.objects.get(pk=obj['toid_id']))
            
        return prereq_list

    def __str__(self):
        return self.name

class CourseHasPrerequisite(models.Model):
    fromid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id1') #foreign key CourseIDa
    toid = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id2') #foreign key CourseID

    def get_name_from_id(self):
        all_objects = Course.objects.filter(id=self['toid_id'])
        name_list = []
        for obj in all_objects:
            name_list.append(obj.name)
        return name_list
        #all_objects = Course.objects.filter(id = self.toid_id)
        #ret_list = []
        #for obj in all_objects:
        #    print(obj)
        #    ret_list.append(obj.name)
        #return ret_list

    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseid = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.IntegerField()

    def __str__(self):
        return self.name


        