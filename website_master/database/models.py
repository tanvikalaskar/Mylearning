from django.db import models

class Category(models.Model):
    cat_id = models.CharField(max_length = 10)
    cat_name = models.CharField(max_length = 10)

class Student(models.Model):
    student_id = models.CharField(max_length = 10)
    student_name = models.CharField(max_length = 30)
    student_password = models.CharField(max_length = 20)
    student_email = models.CharField(max_length = 30)
    student_gradelevel = models.CharField(max_length = 2)

class Teacher(models.Model):
    teacher_id = models.CharField(max_length = 10)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Course(models.Model):
    course_id = models.CharField(max_length = 10)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 20)

class Enrollment(models.Model):
    enrollement_courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_courseid = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled = models.BooleanField()
    e_completion = models.BooleanField()
    grade = models.FloatField()

class Lesson(models.Model):
    lessons_id = models.CharField(max_length = 10)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
 
class Assessment(models.Model):
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    completion = models.BooleanField()
    grade = models.FloatField()
    name = models.CharField(max_length=30)

class Learning(models.Model):
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    completion = models.BooleanField()
    name = models.CharField(max_length=30)


 