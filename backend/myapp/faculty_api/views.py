from django.shortcuts import render, redirect
from myapp.models import Faculty, Faculty_Profile, FacultyPasswordResetToken, JobApplication, JobPost
from .serializers import  FacultySerializer,  FacultyProfileSerializer, FacultyPasswordResetTokenSerializer, JobApplicationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from cloudinary.uploader import upload
from django.core.mail import send_mail
import secrets
from myapp.validation import validate_signup_data
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
import jwt
import os



# creating a signup api for faculty using api_view 
@api_view(['POST'])
@csrf_exempt
def faculty_signup(request):
    if request.method == 'POST':
        user_email = request.data.get('email')     #fetching user email.
        # request.data._mutable = True   #with thid code queryset converted into mutable form
        data = request.data    #storing all sended data in data variable
        data = data.copy()    #make a copy of data in data variable.
        hashed_password = make_password(data.get('password'))  # hashing password
        data['password'] = hashed_password         #updating old password with hashed password
        
        serializer = FacultySerializer(data=data)
        if serializer.is_valid():
            
            # validating username using own validation function.
            validate_signup_data(serializer.validated_data, Faculty)
            
            #saving serializer data to database
            serializer.save()
            
            if serializer.save():
                # Compose email message
                subject = 'Welcome to Our Platform!'
                body = 'Thank you for signing up. We are excited to have you on board!'
                sender_email = 'yadav.parishram@gmail.com'  # Replace with your sender email address
                recipient_email = user_email

                # Send email
                send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,)
                
            return Response({"message":"Your account has been created", "user":serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# Creating login api for faculty using api_view decorator
@api_view(['POST'])
@csrf_exempt
def faculty_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = Faculty.objects.get(username=username)     #fetch user data from database using username
        password_stored_in_db = user_obj.password             # storing password from user_obj in variable.
        match_password = check_password(password,password_stored_in_db)     #matching userpassword and db password 
        
        
        # if password matched then allow user logged in successfully..
        if match_password:
            # user data for creating token.
            payload = {
                'user_id': user_obj.id,
                'username': user_obj.username,
                'email': user_obj.email,
            }
            
            # generate token using payload.
            token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
            
            # storing token in access_token column
            user_obj.access_token = token
            
            # saving user_onj in database.
            user_obj.save()
            return Response({'message': 'You are successfully logged in', 'user': FacultySerializer(user_obj).data}, status=status.HTTP_200_OK)
        
        # if user's password not matched then through error...
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    
    
    
    
# creating api for storing faculty_profile in database.
@api_view(['POST'])
@csrf_exempt
def create_faculty_profile(request):
    if request.method == 'POST':
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
            
            return Response({"message":"your account is created successfully", "serializer data":serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
# logour api using api_view decorator
@api_view(['POST'])
def faculty_logout(request):
    
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    

# creating api for fetching data from database and show it to faculty_profile 
@api_view(['GET'])
@csrf_exempt
def get_faculty_profile(request, pk):
    if request.method == 'POST':
        try:
            faculty_profile = Faculty_Profile.objects.get(id=pk)
            serializer = FacultyProfileSerializer(faculty_profile)
            return Response(serializer.data)
        
        except Faculty_Profile.DoesNotExist:
            return Response({"message": "Profile not found."}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


# creating a update api for faculty_profile
@api_view(['PATCH'])
@csrf_exempt
def update_faculty_profile(request, pk):
    if request.method == 'POST':
        try:
            # current_user = request.user
            # user_id = current_user.id
            profile = Faculty_Profile.objects.get(id=pk)
            
        except Faculty_Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = FacultyProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Your profile has been updated.", "profile_data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


@api_view(['GET'])
@csrf_exempt
def get_faculty_list(request):
    if request.method == 'POST':
        try:
            faculty_list = Faculty_Profile.objects.all()
            print(faculty_list)
            pagination_class = CustomPagination()
            result_page = pagination_class.paginate_queryset(faculty_list, request)
            serializer = FacultyProfileSerializer(result_page, many=True)
            return pagination_class.get_paginated_response(serializer.data)
        
        except Faculty_Profile.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        
        
# forget_password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def forget_password(request):
    if request.method == 'POST':
        user_email = request.data.get('email')
        
        try:
            user = Faculty.objects.get(email = user_email)
            print(user.id)
        except Faculty.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # generate token using secret module.
        token = secrets.token_urlsafe(25)
        
        try:
            FacultyPasswordResetToken.objects.create(user=user, token=token)
        except:
            return Response({"error":"Token not found."})
        
        
        subject = 'f you did not request a new password, please ignore this message.'
        body = f'Please click the following link to reset your password: http://127.0.0.1:8000/reset_password/{token}'
        sender_email = 'yadav.parishram@gmail.com'  # email id of sender mail
        recipient_email = user_email

        # Send email
        send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,)
        
        return Response({"message":"Your reset password email is heading your way."}, status=status.HTTP_201_CREATED)   

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# reset password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def reset_password(request, token):
    if request.method == 'POST':
        try:
            new_password = request.data.get('new_password')
            print(new_password)
        except:
            return Response({"error":"Please enter new password..."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            reset_token_object = FacultyPasswordResetToken.objects.get(token=token)
        except:
            return Response({"error":"User not found, Please try again."}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            if reset_token_object.is_expired():
                return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
            
            hashed_new_password = make_password(new_password)
            user = reset_token_object.user
            user_data = Faculty.objects.get(id=user.id)
            
            user_data.password = hashed_new_password
            user_data.save()
            reset_token_object.delete()
            return Response({"message":"Your password has been changed."})
            
        except FacultyPasswordResetToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    

# creating api for job apply by faculty.
@api_view(['POST'])
@csrf_exempt
def job_apply_by_faculty(request, job_post_id, faculty_profile_id):
    
    if request.method == 'POST':
        
        # fetching faculy obj who already apply on the job.
        faculty_already_applied_on_job_post = JobApplication.objects.get(job_post=job_post_id, faculty_profile=faculty_profile_id)
        print(faculty_already_applied_on_job_post.email)
        
        # checking if faculty already apllied on this job then return faculty only is apllied on this job post.
        if faculty_already_applied_on_job_post:
            return Response({"message":"Candidate Already Apllied On This Job Post."}, status=status.HTTP_409_CONFLICT)
        
        
        data = request.data
        data['job_post'] = job_post_id
        data['faculty_profile'] = faculty_profile_id
        applicant_email = data['email']           # email which faculty give at the time of applying job.
        applicant_name = data['applicant_name']   # apllicant name, who apply for this job
        
        serializer = JobApplicationSerializer(data=data)
        
        if serializer.is_valid():
            item = serializer.save()
            
            # resume
            resume = request.POST.get('resume', False)
            
            try:
                if resume:
                    
                    # uploading resume image to cloudinary
                    upload_resume = upload(resume)
                    
                    # fetching url of resume pdf from cloudinary response
                    item.resume = upload_resume.get('secure_url')
            
            except JobApplication.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            # saving serializer.data to database
            item.save()
            
            job_post_obj = JobPost.objects.get(pk=job_post_id)
            college_profile_obj = job_post_obj.college_profile            #getting object of college_prfile
            college_email = college_profile_obj.email                     #getting email of college from  college_profile 
            college_name = college_profile_obj.college_name               #getting college name from college_profile
            college_profile_id = college_profile_obj.college_id           #getting college_profile_id from college_profile.
            
            
            if college_email:
                subject = f'{applicant_name} apply for a job. Now you can connect with him/her with {applicant_email} email id.'
                body = f'Please click the following link to to check the candidate profile: http://127.0.0.1:8000/get_faculty_profile/{faculty_profile_id}'
                sender_email = 'yadav.parishram@gmail.com'  # email id of sender mail
                recipient_email = college_email
            
                # Send email to college for insforming them that someone apply for a job into your college.
                send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,)

                
            if applicant_email:
                subject = f'Your application is send successfully to the college {college_name}'
                body = f'Please click the following link to to check the College profile: http://127.0.0.1:8000/get_college_profile/{college_profile_id}'
                sender_email = 'yadav.parishram@gmail.com'  # email id of sender mail
                recipient_email = applicant_email

                # Send email to faculty for insforming them that there mail is sended successfully to the college.
                send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,) 

            return Response({"message":"Application is send successfully.", "data":serializer.data}, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
