from django.db import models

class Category(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    gradelevel = models.CharField(max_length = 2)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.course_name
    
class Enrollment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled = models.BooleanField()
    e_completion = models.BooleanField()
    grade = models.FloatField()

    def __str__(self):
        return self.student_id
class Lesson(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
 
    def __str__(self):
        return self.name
    
class Assessment(models.Model):
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    completion = models.BooleanField()
    grade = models.FloatField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Learning(models.Model):
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    completion = models.BooleanField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


 