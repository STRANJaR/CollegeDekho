from django.contrib import admin
from .models import College, Faculty, Student, Faculty_Profile, College_Profile



# admin for colleges
@admin.register(College)
class CollegeModelAdmin(admin.ModelAdmin):
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
    list_display = ["faculty", 'name', 'skills', 'experience', 'avtar', 'qualification', 'about']
    
    
# admin for subject_teacher
# @admin.register(Subject_Teacher)
# class SubjectTeacherModelAdmin(admin.ModelAdmin):
#     list_display = ['college_code', 'subject', 'qualification', 'additional_skills', 'experience_years']
    
   
# admin for college_profile 
@admin.register(College_Profile)
class CollegeProfileModelAdmin(admin.ModelAdmin):
    list_display = ['college', 'college_name', 'logo', 'images', 'description', 'location', 'established_date', 'website', 'student_population', 'faculty_population', 'affiliated_by', 'college_type', 'college_code']
    