from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=255) 
    name = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    semester_name = models.CharField(max_length=255)
    semester_type = models.CharField(null=True, max_length=255)
    ects = models.IntegerField()
    description = models.TextField(null=True)
    teaching_language = models.CharField(max_length=255)
    has_prerequisite = models.IntegerField()

    def get_prerequisite(self):
        all_objects = CourseHasPrerequisite.objects.filter(course_id=self.id) #lika her
        prereq_list = []
        for obj in all_objects.values():
            prereq_list.append(Course.objects.get(pk=obj['prereq_id_id'])) #gæti verið að vanti _id
        return prereq_list
    
    def get_semester(self):
        all_objects = CourseSemester.objects.filter(courseid=self.id)
        semester_list = []
        for obj in all_objects:
            semester_list.append(obj)
        return semester_list

    def __str__(self):
        return self.course_code

class CourseHasPrerequisite(models.Model):
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id1') #foreign key CourseIDa
    prereq_id = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='id2') #foreign key CourseID
    parallel_enrollment = models.IntegerField(default=0)


    # def get_name_from_id(self):
    #     all_objects = Course.objects.filter(id=self['to_id'])
    #     name_list = []
    #     for obj in all_objects:
    #         name_list.append(obj.name)
    #     return name_list

    def __str__(self):
        course = self.prereq_id
        return course.course_code

class Semesters(models.Model):
    description = models.CharField(max_length=63)

    def __str__(self):
        return self.description
    

class CourseSemester(models.Model):
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE) #foreign key CourseID
    semesterid = models.ForeignKey(Semesters, on_delete = models.CASCADE)

    def __str__(self):
        return self.course_id

#class Label(models.Model):
#    label_name = models.CharField()

#    def __str__(self):
#        return self.label_name