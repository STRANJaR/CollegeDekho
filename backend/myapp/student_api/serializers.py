from myapp.models import Student
from rest_framework import serializers

        
    
# serializer for student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'password']
        
        