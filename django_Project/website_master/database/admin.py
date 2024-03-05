from django.contrib import admin
from .models import Teacher,Student,Enrollment,Lesson,Category,Course,Assessment,Learning

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'email', 'gradelevel')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'student_id', 'enrolled', 'e_completion', 'grade')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseid', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'teacher_id', 'course_name')

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('lessonid', 'studentid', 'completion', 'grade', 'name')

class LearningAdmin(admin.ModelAdmin):
    list_display = ('lessonid', 'studentid', 'completion', 'name')

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Learning, LearningAdmin)