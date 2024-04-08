from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from datetime import datetime, timedelta

# model for college
class College(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    
    
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
    name = models.CharField(max_length=100)
    skills = models.TextField(max_length=1500)
    experience = models.TextField(max_length=1500)
    avtar = models.ImageField(upload_to='profile_pictures/', default="profile pic not found")
    qualification = models.TextField(max_length=2000, default="")
    about = models.TextField(max_length=2000, default="")
    
    # username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    
# creating model for college_profile
class College_Profile(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE, primary_key=True, default="")
    college_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo_images/', default="Image not found")
    images = models.ImageField(upload_to='college_images/', default="Image not found")
    description = models.TextField(max_length=1500)
    location = models.TextField(max_length=1000)
    established_date = models.DateField()
    website = models.URLField()
    student_population = models.PositiveIntegerField()
    faculty_population = models.PositiveIntegerField()
    affiliated_by = models.TextField(max_length=500, null=False)
    
    # giving choices
    my_choices = [
        ('IT', 'IT'),
        ('Non-IT', 'Non-IT'),
        ("Both", 'Both'),
        ('Others','Others')
    ]
    college_type = models.CharField(max_length=50, choices=my_choices, default="")
    college_code = models.CharField(max_length=50, null=False)
    
    


# class Subject_Teacher(models.Model):
#     college_code = models.ForeignKey(College_Profile, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=300)
#     qualification = models.TextField(max_length=1000)
#     additional_skills = models.TextField(max_length=1000)
#     experience_years = models.IntegerField()
    
    
class CollegePasswordResetToken(models.Model):
    user = models.ForeignKey(College, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)
    
    
class FacultyPasswordResetToken(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)
    

class StudentPasswordResetToken(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=5)
