from django.db import models



# model for college
class College(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=100)
    
    
    
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
    picture = models.ImageField(upload_to='profile_pictures/')
    # username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    
# creating model for college_profile
class College_Profile(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo_images/', default="Image not found")
    college_image = models.ImageField(upload_to='college_images/', default="Image not found")
    description = models.TextField(max_length=1500)
    location = models.TextField(max_length=1000)
    established_date = models.DateField()
    website = models.URLField()
    student_population = models.PositiveIntegerField()
    faculty_population = models.PositiveIntegerField()
    


class Subject_Teacher(models.Model):
    college_id = models.ForeignKey(College_Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    qualification = models.TextField(max_length=1000)
    additional_skills = models.TextField(max_length=1000)
    experience_years = models.IntegerField()