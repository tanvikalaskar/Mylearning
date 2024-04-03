from django.urls import path

from .views import SignUpView

from .views import TeacherSignUpView

urlpatterns = [
    path("newStudent/", SignUpView.as_view(), name="newStudent"),
    path("newTeacher/", TeacherSignUpView.as_view(), name = "newTeacher"),
]
