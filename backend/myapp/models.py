from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from datetime import datetime, timedelta

# model for college
class College(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    access_token = models.CharField(max_length=200, null=False, default="")
    
    
# model for faculty
class Faculty(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100)
    

# model for student    
class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100)
    

# model for FACULTY profile.
class Faculty_Profile(models.Model):
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE,primary_key=True, default='')
    name = models.CharField(max_length=100)
    skills = models.TextField(max_length=1500)
    experience = models.TextField(max_length=1500)
    avtar = models.ImageField(upload_to='profile_pictures/', default="profile pic not found")
    qualification = models.TextField(max_length=2000, default="")
    about = models.TextField(max_length=2000, default="")
    email = models.EmailField(null=False, default="")
    # username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    
# creating model for college_profile
class College_Profile(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE, primary_key=True, default="")
    college_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo_images/', default="Image not found")
    images = models.ImageField(upload_to='college_images/', default="Image not found")
    description = models.TextField(max_length=700)
    location = models.TextField(max_length=300)
    established_date = models.DateField()
    website = models.URLField()
    student_population = models.PositiveIntegerField()
    faculty_population = models.PositiveIntegerField()
    affiliated_by = models.TextField(max_length=500, null=False)
    created_date = models.DateField(auto_now=True)
    
    
    # giving choices
    my_choices = [
        ('IT', 'IT'),
        ('Non-IT', 'Non-IT'),
        ("Both", 'Both'),
        ('Others','Others')
    ]
    college_type = models.CharField(max_length=50, choices=my_choices, default="")
    college_code = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, default="")
    
    

# creating model for collge_password_reset_token. 
class CollegePasswordResetToken(models.Model):
    user = models.ForeignKey(College, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)
    
    
# creating model for faculty_password_reset_token.
class FacultyPasswordResetToken(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)
    


#creating model for student_password_reset_token. 
class StudentPasswordResetToken(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)


# creating profile for job_post of college.
class JobPost(models.Model):
    college_profile = models.ForeignKey(College_Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    description = models.TextField(null=True)
    vacancy_available = models.IntegerField(default=1)
    skills_required = models.TextField(max_length=500, null=True)
    about_work = models.TextField(max_length=500)
    who_can_apply = models.TextField(max_length=300)
    additional_information = models.TextField(max_length=200, null=True)
    
    
    
class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    faculty_profile = models.ForeignKey(Faculty_Profile, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.CharField(max_length=200)
    