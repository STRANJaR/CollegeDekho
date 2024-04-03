from myapp.models import Faculty, Faculty_Profile
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
        
    

        
    
