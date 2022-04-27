from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=63)
    ects = models.IntegerField()

    def __str__(self):
        return self.name

class CourseHasPrerequisite(models.Model):
    fromID = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id1') #foreign key CourseIDa
    toID = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id2') #foreign key CourseID

    def __str__(self):
        return self.name

class CourseSemester(models.Model):
    courseID = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterID = models.CharField(max_length=63)

    def __str__(self):
        return self.name