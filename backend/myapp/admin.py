from django.contrib import admin
from .models import User, Faculty, Student, Faculty_Profile, College_Profile, Subject_Teacher



# admin for colleges
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    

# admin for faculty
@admin.register(Faculty)
class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    

# admin for student
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']
    
    
# admin for faculty_profile
@admin.register(Faculty_Profile)
class FacultyProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skills', 'experience', 'picture']
    
    
# admin for subject_teacher
@admin.register(Subject_Teacher)
class SubjectTeacherModelAdmin(admin.ModelAdmin):
    list_display = ['college_id', 'subject', 'qualification', 'additional_skills', 'experience_years']
    
   
# admin for college_profile 
@admin.register(College_Profile)
class CollegeProfileModelAdmin(admin.ModelAdmin):
    list_display = ['college_id', 'college_name', 'logo', 'college_image', 'description', 'location', 'established_date', 'website', 'student_population', 'faculty_population']
    