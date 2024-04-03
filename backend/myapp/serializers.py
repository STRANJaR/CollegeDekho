# from .models import College, Faculty, Student, Faculty_Profile, College_Profile, Subject_Teacher
# from rest_framework import serializers


# # serializer for college
# class CollegeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = College
#         fields = ['id', 'username', 'email', 'password']
        
# # serializer for faculty
# class FacultySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Faculty
#         fields = ['id', 'username', 'email', 'password']
        
    
# # serializer for student
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'username', 'email', 'password']
        
        
# # serializer for Faculty_Profile
# class FacultyProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Faculty_Profile
#         fields = '__all__'
        
    
# # serializer for college_profile
# class CollegeProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = College_Profile
#         fields = '__all__'
        
    
# # serializer for subject_teacher
# class SubjectTeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject_Teacher
#         fields = '__all__'