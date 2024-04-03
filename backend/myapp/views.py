# from django.shortcuts import render, redirect
# from .models import College, Faculty, Student, Faculty_Profile, Subject_Teacher, College_Profile
# from .serializers import CollegeSerializer, FacultySerializer, StudentSerializer , FacultyProfileSerializer, CollegeProfileSerializer, SubjectTeacherSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_protect, csrf_exempt
# from .pagination import CustomPagination


# # Creating signup api for college using api_view decorator
# @api_view(['POST'])
# @csrf_exempt
# def college_signup(request): 
#     serializer = CollegeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Creating login api for college using api_view decorator
# @api_view(['POST'])
# @csrf_exempt
# def college_login(request):
#     if not request.user.is_authenticated:
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = College.objects.get(username=username, password=password)
#         if user:
#             return Response({'message': 'Login successful', 'user': CollegeSerializer(user).data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     else:
#         return Response("You are already Logged In.")
        
        

# # creating a signup api for faculty using api_view 
# @api_view(['POST'])
# @csrf_exempt
# def faculty_signup(request):
#     serializer = FacultySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Creating login api for faculty using api_view decorator
# @api_view(['POST'])
# @csrf_exempt
# def faculty_login(request):
#     if not request.user.is_authenticated:
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = Faculty.objects.get(username=username, password=password)
#         if user:
#             return Response({'message': 'Login successful', 'user': CollegeSerializer(user).data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     else:
#         return Response("You are already Logged In.")
    
    
    

# # creating a signup api for Student using api_view 
# @api_view(['POST'])
# @csrf_exempt
# def Student_signup(request):
#     if request.user.is_authenticated:
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# # Creating login api for Student using api_view decorator
# @api_view(['POST'])
# @csrf_exempt
# def Student_login(request):
#     if request.user.is_authenticated:
#         if not request.user.is_authenticated:
#             username = request.data.get('username')
#             password = request.data.get('password')
#             print(username)
#             print(password)
#             user = Student.objects.get(username=username, password=password)
#             if user:
#                 return Response({'message': 'Login successful', 'user': CollegeSerializer(user).data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response("You are already Logged In.")
    
#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    

# # creating api for storing faculty_profile in database.
# @api_view(['POST'])
# @csrf_exempt
# def create_faculty_profile(request):
#     # if request.user.is_authenticated:
#     serializer = FacultyProfileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # else:
#     #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    

# # creating api for fetching data from database and show it to faculty_profile 
# @api_view(['GET'])
# @csrf_exempt
# def get_faculty_profile_data(request, pk):
#     # if request.user.is_authenticated:
#     try:
#         faculty_profile = Faculty_Profile.objects.get(id=pk)
#         serializer = FacultyProfileSerializer(faculty_profile)
#         return Response(serializer.data)
    
#     except Faculty_Profile.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     # else:
#     #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# # creating a update api for faculty_profile
# @api_view(['PATCH'])
# @csrf_exempt
# def update_faculty_profile(request, pk):
#     if request.user.is_authenticated:
#         try:
#             # current_user = request.user
#             # user_id = current_user.id
#             profile = Faculty_Profile.objects.get(id=pk)
            
#         except Faculty_Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = FacultyProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# # creating a api for collegeProfile 
# @api_view(['POST'])
# @csrf_protect
# def create_college_profile(request):
#     if request.user.is_authenticated:
#         serializer = CollegeProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
    
# # api for college_list using api_view decorator
# @api_view(['GET'])
# @csrf_exempt
# def college_list(request):
#     try:
#         college_list = College_Profile.objects.all()
#         print(college_list)
#         serializer = CollegeProfileSerializer(college_list, many=True)
#         return Response(serializer.data)
    
#     except College_Profile.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST) 



# # creating get api for  colleg_profile
# @api_view(['GET'])
# def get_college_profile_data(request, pk):
#     if request.user.is_authenticated:
#         try:
#             # id = request.user.id
#             college_profile = College_Profile.objects.get(id=pk)
#             serializer = CollegeProfileSerializer(college_profile)
#             return Response(serializer.data)
            
#         except Faculty_Profile.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    

# # creating a update api for college_profile
# @api_view(['PATCH'])
# @csrf_exempt
# def update_college_profile(request, pk):
#     if request.user.is_authenticated:
#         try:
#             # current_user = request.user
#             # user_id = current_user.id
#             profile = College_Profile.objects.get(id=pk)
#             print(profile)
#         except College_Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
            
#         serializer = CollegeProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    

# @api_view(['GET'])
# @csrf_exempt
# def get_faculty_list(request):
#     try:
#         faculty_list = Faculty_Profile.objects.all()
#         pagination_class = CustomPagination()
#         result_page = pagination_class.paginate_queryset(faculty_list, request)
#         serializer = FacultyProfileSerializer(result_page, many=True)
#         return pagination_class.get_paginated_response(serializer.data)
    
#     except Faculty_Profile.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)