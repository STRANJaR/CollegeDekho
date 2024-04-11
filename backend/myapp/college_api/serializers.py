from myapp.models import College, College_Profile, CollegePasswordResetToken, JobPost
from rest_framework import serializers


# serializer for college
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'username', 'email', 'password']
        

    
# serializer for college_profile
class CollegeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = College_Profile
        fields = '__all__'
        
    
# serializer for job post by college
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
            
        
class CollegePasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePasswordResetToken
        fields = "__all__"
    
    

        
    
