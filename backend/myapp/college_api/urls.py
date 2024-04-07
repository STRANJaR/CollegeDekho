from django.urls import path
from myapp.college_api import views


urlpatterns = [
    path('college_signup/', views.college_signup, name="college_signup"),
    path('college_login/', views.college_login, name="college_login"),
    path('create_college_profile/', views.create_college_profile, name="create_college_profile"),
    path('get_college_profile/<int:pk>', views.get_college_profile_data, name="get_college_profile"),
    path('update_college_profile/<int:pk>', views.update_college_profile, name="update_college_profile"),
    path('get_college_list/', views.get_college_list, name="college_list"),
    path('college_forget_password/', views.forget_password, name="forget_password"),
    path('college_reset_password/<token>', views.reset_password, name="reset_password"),
]
