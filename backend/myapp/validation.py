from rest_framework import serializers
from .models import College, Faculty, Student
import re
from rest_framework.response import Response



# validation function.
def validate_signup_data(data, model_name):
    username = data.get('username')
    password = data.get('password')
    
    # Check if username or email is already taken
    if model_name.objects.filter(username=username).exists():
        raise serializers.ValidationError("Username is already taken")
    
    
    # Check if password is already taken
    if model_name.objects.filter(password=password).exists():
        raise serializers.ValidationError("password is already taken")
    
    
    # validating password should be greater then 8 character
    if len(password) < 8:
        raise serializers.ValidationError("password must be at least 8 characters long")
    
    
    # validating password should contain letter, numbers and uppercase, lowercase and special character
    # if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>])[A-Za-z\d!@#$%^&*()\-_=+{};:,<.>]{8,}$", password):
    #     raise serializers.ValidationError("Password must contain at least one alphanumeric character and one special character and atleast 8 character long.")
    
    
    # validating username should be greater then 8 character
    if len(username) < 8:
        raise serializers.ValidationError("username must be at least 8 characters long")
        
        
    # validating username should be alphanumeirc character . 
    if not re.match("^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9!@#$%^&*()_+=\-[\]{}<>/?\\|]*$", username):
        raise serializers.ValidationError("username must contain both letters and numbers")
        
    
    