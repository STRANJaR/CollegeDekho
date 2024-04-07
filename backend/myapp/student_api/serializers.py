from myapp.models import Student, StudentPasswordResetToken
from rest_framework import serializers

        
    
# serializer for student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'password']
        
        
class StudentPasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPasswordResetToken
        fields = "__all__"
        