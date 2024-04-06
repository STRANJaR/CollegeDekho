from django.shortcuts import render, redirect
from myapp.models import Faculty, Faculty_Profile
from .serializers import  FacultySerializer,  FacultyProfileSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from cloudinary.uploader import upload



# creating a signup api for faculty using api_view 
@api_view(['POST'])
@csrf_exempt
def faculty_signup(request):
    request.data._mutable = True   #with thid code queryset converted into mutable form
    data = request.data    #storing all sended data in data variable
    hashed_password = make_password(data.get('password'))  # hashing password
    data['password'] = hashed_password         #updating old password with hashed password
    
    serializer = FacultySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Your signup is done successfull", "serializer data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Creating login api for faculty using api_view decorator
@api_view(['POST'])
@csrf_exempt
def faculty_login(request):
    if not request.user.is_authenticated:
        username = request.data.get('username')
        password = request.data.get('password')
        user = Faculty.objects.get(username=username, password=password)
        if user:
            return Response({'message': 'Login successful', 'user': FacultySerializer(user).data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        return Response("You are already Logged In.")
    
    
    
# creating api for storing faculty_profile in database.
@api_view(['POST'])
@csrf_exempt
def create_faculty_profile(request):
    # if request.user.is_authenticated:
    serializer = FacultyProfileSerializer(data=request.data)
    if serializer.is_valid():
        
        item = serializer.save()
        
        # faculty profile picture
        profile_pic = request.POST.get('avtar', False)
        
        try:
            if profile_pic:
                # uploading facuty profile to cloudinary
                upload_image = upload(profile_pic)
                
                # fetching url of college image from cloudinary response
                item.avtar = upload_image.get('url')
                
        except Faculty_Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        item.save()
        
        # message = "Your profile is created successfuly..."
        
        return Response({"message":"successfull", "serializer data":serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    

# creating api for fetching data from database and show it to faculty_profile 
@api_view(['GET'])
@csrf_exempt
def get_faculty_profile(request, pk):
    # if request.user.is_authenticated:
    try:
        faculty_profile = Faculty_Profile.objects.get(id=pk)
        serializer = FacultyProfileSerializer(faculty_profile)
        return Response(serializer.data)
    
    except Faculty_Profile.DoesNotExist:
        return Response({"message": "faculty with this id is does not exist..."}, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# creating a update api for faculty_profile
@api_view(['PATCH'])
@csrf_exempt
def update_faculty_profile(request, pk):
    # if request.user.is_authenticated:
    try:
        # current_user = request.user
        # user_id = current_user.id
        profile = Faculty_Profile.objects.get(id=pk)
        
    except Faculty_Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = FacultyProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['GET'])
@csrf_exempt
def get_faculty_list(request):
    try:
        faculty_list = Faculty_Profile.objects.all()
        print(faculty_list)
        pagination_class = CustomPagination()
        result_page = pagination_class.paginate_queryset(faculty_list, request)
        serializer = FacultyProfileSerializer(result_page, many=True)
        return pagination_class.get_paginated_response(serializer.data)
    
    except Faculty_Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)