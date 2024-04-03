from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('college_signup/', views.college_signup, name="college_signup"),
    # path('college_login/', views.college_login, name="college_login"),
    # path('faculty_signup/', views.faculty_signup, name="faculty_signup"),
    # path('faculty_login/', views.faculty_login, name="faculty_login"),
    # path('student_signup/', views.faculty_signup, name="student_signup"),
    # path('student_login/', views.faculty_login, name="student_login"),
    # path('create_faculty_profile/', views.create_faculty_profile, name="create_faculty_data"),
    # path('get_faculty_data/<int:pk>', views.get_faculty_profile_data, name="get_faculty_data"),
    # path('update_faculty_profile/<int:pk>', views.update_faculty_profile, name="update_faculty_file"),
    # path('create_college_profile/', views.create_college_profile, name="create_college_profile"),
    # path('get_college_profile/<int:pk>', views.get_college_profile_data, name="get_college_profile"),
    # path('update_college_profile/<int:pk>', views.update_college_profile, name="update_college_profile"),
    # path('college_list/', views.college_list, name="college_list"),
    # path('get_faculty_list/', views.get_faculty_list, name="faculty_list"),
    path('', include('myapp.college_api.urls')),
    path('', include('myapp.faculty_api.urls')),
    path('', include('myapp.student_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)