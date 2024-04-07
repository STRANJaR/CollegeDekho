from myapp.models import Faculty, Faculty_Profile, FacultyPasswordResetToken
from rest_framework import serializers



        
# serializer for faculty
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'username', 'email', 'password']
        
    
    
# serializer for Faculty_Profile
class FacultyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_Profile
        fields = '__all__'
        
    
class FacultyPasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyPasswordResetToken
        fields = "__all__"

        
    
