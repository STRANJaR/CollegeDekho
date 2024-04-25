from django.urls import path
from myapp.student_api import views

urlpatterns = [
    path('student_signup/', views.student_signup, name="student_signup"),
    path('student_logout/', views.student_logout, name="student_logout"),
    path('student_login/', views.student_login, name="student_login"),
    path('student_forget_password/', views.forget_password, name="forget_password"),
    path('student_reset_password/<token>/', views.reset_password, name="reset_password"),
]
