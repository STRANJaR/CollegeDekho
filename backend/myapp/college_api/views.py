from django.shortcuts import render, redirect
from myapp.models import College, Subject_Teacher, College_Profile
from .serializers import CollegeSerializer, CollegeProfileSerializer, SubjectTeacherSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from cloudinary.uploader import upload


# Creating signup api for college using api_view decorator
@api_view(['POST'])
@csrf_exempt
def college_signup(request): 
    request.data._mutable = True   #with this code queryset converted into mutable form
    data = request.data    #storing all sended data in data variable
    hashed_password = make_password(data.get('password'))  # hashing password
    data['password'] = hashed_password         #updating old password with hashed password
    
    serializer = CollegeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Your signup is done successfuly", "data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Creating login api for college using api_view decorator
@api_view(['POST'])
@csrf_exempt
def college_login(request):
    if not request.user.is_authenticated:
        username = request.data.get('username')
        password = request.data.get('password')
        user = College.objects.get(username=username, password=password)
        if user:
            return Response({'message': 'Login successful', 'user': CollegeSerializer(user).data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        return Response("You are already Logged In.")
        
            


# creating a api for collegeProfile 
@api_view(['POST'])
@csrf_exempt
def create_college_profile(request):
    # if request.user.is_authenticated:
    serializer = CollegeProfileSerializer(data=request.data)
    if serializer.is_valid():
        item = serializer.save()
        
        # college image
        image = request.POST.get('images', False)
        
        # college logo 
        logo = request.POST.get('image', False)
        
        try:
            if image:
                # uploading college image to cloudinary
                upload_image = upload(image)
                
                # fetching url of college image from cloudinary response
                item.images = upload_image.get('secure_url')
                
        except College_Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if logo:
                # uploading college image to cloudinary
                upload_logo = upload(logo)
                
                # fetching url of college image from cloudinary response and store it in database
                item.logo = upload_logo.get('secure_url')
                
        except College_Profile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # saving serializer.data to database
        item.save()
        
        return Response({"message":"Your signup is done successfuly", "serialized data":serializer.data}, status=status.HTTP_201_CREATED)
        
        
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    
    
# api for college_list using api_view decorator
@api_view(['GET'])
@csrf_exempt
def get_college_list(request):
    try:
        college_list = College_Profile.objects.all()
        pagination_class = CustomPagination()
        result_page = pagination_class.paginate_queryset(college_list, request)
        serializer = CollegeProfileSerializer(result_page, many=True)
        return pagination_class.get_paginated_response(serializer.data)
    
    except College_Profile.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST) 



# creating get api for  colleg_profile
@api_view(['GET'])
def get_college_profile_data(request, pk):
    # if request.user.is_authenticated:
    try:
        college_profile = College_Profile.objects.get(id=pk)
        serializer = CollegeProfileSerializer(college_profile)
        return Response(serializer.data)
        
    except College_Profile.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    

# creating a update api for college_profile
@api_view(['PATCH'])
@csrf_exempt
def update_college_profile(request, pk):
    # if request.user.is_authenticated:
    try:
        profile = College_Profile.objects.get(id=pk)
        print(profile)
    except College_Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = CollegeProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    

