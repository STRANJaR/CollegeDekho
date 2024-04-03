from django.urls import path
from myapp.student_api import views

urlpatterns = [
    path('student_signup/', views.student_signup, name="student_signup"),
    path('student_login/', views.student_login, name="student_login"),
]
