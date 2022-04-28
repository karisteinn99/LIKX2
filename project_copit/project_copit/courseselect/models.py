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

    #gera föll td ná í undanfara á x áfanga

    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseid = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.IntegerField()

    def __str__(self):
        return self.name