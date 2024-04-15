from django.urls import path
from myapp.college_api import views


urlpatterns = [
    path('college_signup/', views.college_signup, name="college_signup"),
    path('college_logout/', views.college_logout, name="college_logout"),
    path('college_login/', views.college_login, name="college_login"),
    path('create_college_profile/<int:user_id>/', views.create_college_profile, name="create_college_profile"),
    path('get_college_profile/<int:pk>/', views.get_college_profile_data, name="get_college_profile"),
    path('update_college_profile/<int:pk>/', views.update_college_profile, name="update_college_profile"),
    path('get_college_list/', views.get_college_list, name="college_list"),
    path('college_forget_password/', views.forget_password, name="forget_password"),
    path('college_reset_password/<token>/', views.reset_password, name="reset_password"),
    path('job_post_by_college/<int:college_id>/', views.job_post_by_college, name="job_post"),
    path('faculties_apply_on_same_job_post/<int:job_post_id>/', views.faculties_apply_on_same_job_post, name="faculties_apply_on_same_job_post"),
    path('get_job_post/<int:job_post_id>/', views.get_job_post, name="get_job_post"),   
]
