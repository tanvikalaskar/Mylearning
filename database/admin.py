from django.contrib import admin
from .models import Teacher,Student,Enrollment,Lesson,Category,Course,Assessment,Learning

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(Learning)