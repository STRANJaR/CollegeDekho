from django.contrib import admin
from .models import College, Faculty, Student, Faculty_Profile, College_Profile, JobPost



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
    
    
# admin for job post
@admin.register(JobPost)
class JobPostModelAdmin(admin.ModelAdmin):
    list_display = ['college_profile', 'position', 'description', 'vacancy_available', 'skills_required', 'about_work', 'who_can_apply', 'additional_information']
    
    
   
# admin for college_profile 
@admin.register(College_Profile)
class CollegeProfileModelAdmin(admin.ModelAdmin):
    list_display = ['college', 'college_name', 'logo', 'images', 'description', 'location', 'established_date', 'website', 'student_population', 'faculty_population', 'affiliated_by', 'college_type', 'college_code']
    
    
# admin for job application
class JobApplicatioModelAdmin(admin.ModelAdmin):
    list_display = ['job_post', 'faculty_profile', 'applicant_name', 'email', 'resume', 'cover_letter']
    