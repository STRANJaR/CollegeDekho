from django.contrib import admin
from django.urls import path
from myapp.faculty_api import views

urlpatterns = [
    path('get_faculty_list/', views.get_faculty_list, name="faculty_list"),
    path('faculty_signup/', views.faculty_signup, name="faculty_signup"),
    path('faculty_login/', views.faculty_login, name="faculty_login"),
    path('faculty_logout/', views.faculty_logout, name="faculty_login"),
    path('create_faculty_profile/<int:user_id>/', views.create_faculty_profile, name="create_faculty_data"),
    path('get_faculty_profile/<int:pk>/', views.get_faculty_profile, name="get_faculty_data"),
    path('update_faculty_profile/<int:pk>/', views.update_faculty_profile, name="update_faculty_file"),
    path('faculty_forget_password/', views.forget_password, name="forget_password"),
    path('faculty_reset_password/<token>/', views.reset_password, name="reset_password"),
    path('job_apply_by_faculty/<int:job_post_id>/<int:faculty_profile_id>/', views.job_apply_by_faculty, name="job_apply_by_faculty"),
    path('get_colleges_apply_by_faculty/<int:faculty_profile_id>/', views.get_colleges_apply_by_faculty, name="get_colleges_apply_by_faculty"),
]
