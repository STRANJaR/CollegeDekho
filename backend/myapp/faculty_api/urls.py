from django.contrib import admin
from django.urls import path
from myapp.faculty_api import views

urlpatterns = [
    path('get_faculty_list/', views.get_faculty_list, name="faculty_list"),
    path('faculty_signup/', views.faculty_signup, name="faculty_signup"),
    path('faculty_login/', views.faculty_login, name="faculty_login"),
    path('create_faculty_profile/', views.create_faculty_profile, name="create_faculty_data"),
    path('get_faculty_profile/<int:pk>', views.get_faculty_profile, name="get_faculty_data"),
    path('update_faculty_profile/<int:pk>', views.update_faculty_profile, name="update_faculty_file"),
]
