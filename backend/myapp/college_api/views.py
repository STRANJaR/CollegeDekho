from myapp.models import College, College_Profile, CollegePasswordResetToken, JobPost, JobApplication
from .serializers import CollegeSerializer, CollegeProfileSerializer, CollegePasswordResetTokenSerializer, JobPostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from cloudinary.uploader import upload
from django.core.mail import send_mail
from django.contrib.auth import logout
from myapp.validation import validate_signup_data
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from myapp.signals import user_login_failed
import secrets
import jwt
import os


# Creating signup api for college using api_view decorator
@api_view(['POST'])
@csrf_exempt
def college_signup(request): 
    if request.method == 'POST':
        user_email = request.data.get('email')     #fetching user email.
        # request.data._mutable = True   #with this code queryset converted into mutable form
        data = request.data    #storing all sended data in data variable
        data = data.copy()    #make a copy of data in data variable.
        hashed_password = make_password(data.get('password'))  # hashing password
        data['password'] = hashed_password         #updating old password with hashed password
        serializer = CollegeSerializer(data=data)   #serializing data.
        
        if serializer.is_valid():
            
            # validating username using own validation function.
            validate_signup_data(serializer.validated_data, College)
            
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




# Creating login api for college using api_view decorator
@api_view(['POST'])
@csrf_exempt
def college_login(request):
    # if not request.user.is_authenticated:
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user_obj = College.objects.get(username=username)     #fetch user data from database using username
    except College.DoesNotExist:
        # Emit the user_login_failed signal when user does not exist
        user_login_failed.send(sender=College, credentials=user_obj, request=request)        
        return Response({"message":"User Does Not Exist."}, status=status.HTTP_400_BAD_REQUEST)
        
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
        
        
        return Response({'message': 'You are successfully logged in', 'user': CollegeSerializer(user_obj).data, "accessToken":token}, status=status.HTTP_200_OK)
    
    # if user's password not matched then throw this error...
    else:
        # Emit the user_login_failed signal when password does not match
        user_login_failed.send(sender=College, credentials=user_obj, request=request)
        return Response({'message': 'Invalid Password'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
    


# creating a api for collegeProfile 
@api_view(['POST'])
@csrf_exempt
def create_college_profile(request, user_id):
    # if request.user.is_authenticated:
    profile_data = request.data           #storing profile data in profile_data variable.
    profile_data['college'] = user_id       # adding user_id from college model in querydict.
    serializer = CollegeProfileSerializer(data=profile_data)     #serializing profile_data.
    
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
        
        return Response({"message":"Your profile details have been saved.", "profile_data":serializer.data}, status=status.HTTP_201_CREATED)
        
        
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response({"message":"user is unauthorized or no found"}, status=status.HTTP_401_UNAUTHORIZED)
    
    
    
    
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



# logour api using api_view decorator
@api_view(['POST'])
def college_logout(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# creating get api for  colleg_profile
@api_view(['GET'])
def get_college_profile_data(request, pk):
    if request.method == 'POST':
        try:
            college_profile = College_Profile.objects.get(id=pk)
            serializer = CollegeProfileSerializer(college_profile)
            return Response({"data":serializer.data}, status=status.HTTP_302_FOUND)
            
        except College_Profile.DoesNotExist:
            return Response({"message": "Profile not found."}, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    

# creating a update api for college_profile
@api_view(['PATCH'])
@csrf_exempt
def update_college_profile(request, pk):
    if request.method == 'POST':
        try:
            profile = College_Profile.objects.get(id=pk)
        except College_Profile.DoesNotExist:
            return Response({"message":"Profile does not found."}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = CollegeProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Your profile has been updated.", "profile_data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    



# forget_password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def forget_password(request):
    if request.method == 'POST':
        user_email = request.data.get('email')
        
        try:
            user = College.objects.get(email = user_email)

        except College.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # generate token using secret module.
        token = secrets.token_urlsafe(25)
        
        try:
            CollegePasswordResetToken.objects.create(user=user, token=token)
        except:
            return Response({"error":"Token not found."})
        
        
        subject = 'If you did not request a new password, please ignore this message.'
        body = f'Please click the following link to reset your password: http://127.0.0.1:8000/reset_password/{token}/'
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
        except:
            return Response({"error":"Please enter new password..."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            reset_token_object = CollegePasswordResetToken.objects.get(token=token)
        except:
            return Response({"error":"User not found, Please try again. "}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if reset_token_object.is_expired():
                return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
            
            hashed_new_password = make_password(new_password)    #hashing password
            user = reset_token_object.user                      #get user from reset_token_object
            user_data = College.objects.get(id=user.id)         #get user data using user_id 
            
            user_data.password = hashed_new_password           #saving hashed password to main password
            user_data.save()                                   #saving new password to password
            reset_token_object.delete()                       #deleting reset_token_object from token object..
            return Response({"message":"Your password has been changed."})
            
        except CollegePasswordResetToken.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    

# creating api for job post by college.
@api_view(['POST'])
@csrf_exempt
def job_post_by_college(request, college_id):
    if request.method == 'POST':
        data = request.data 
        data = data.copy()
        data['college_profile'] = college_id
        serializer = JobPostSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# all faculties who apply on same job post.
@api_view(['GET'])
@csrf_exempt
def get_faculties_apply_on_same_job_post(request, job_post_id):
    if request.method == 'POST':
        
        # getting job application object with job_post_id
        job_applicaton_obj = JobApplication.objects.filter(job_post=job_post_id)

        
        applicant_name = []        #List for storing applicant name.
        applicant_profile_link = []     #List for storing applicant profile link.
        job_post_link = []        #list for storing job post link.
        
        
        # playing for loop for getting obj from job_application_obj.
        for obj in job_applicaton_obj:
            
            candidate_name = obj.applicant_name        #storing applicant name in candidate variable
            faculty_profile_obj = obj.faculty_profile   #storing faculty profile object in variable
            faculty_obj = faculty_profile_obj.faculty    #storing faculty object in vairable
            faculty_id = faculty_obj.id       #storing faculty id in variable
            
            applicant_name.append(candidate_name)    #appending candidate name in applicant name list
            applicant_profile_link.append(f'http://127.0.0.1:8000/get_faculty_profile/{faculty_id}/')      #appending applicant profile link in applicant_profile_list.
            job_post_link.append(f'http://127.0.0.1:8000/get_job_post/{job_post_id}/')         #appending job post link in job_post_link list.
        
        return Response({"applicant_name":applicant_name, "applicant_profile_link":applicant_profile_link, "job_post_link":job_post_link})
    
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


# get job post by id using api decorator
@api_view(['GET'])
@csrf_exempt
def get_job_post(request,job_post_id):
    if request.method == 'GET':
        try:
            job_post = JobPost.objects.get(id = job_post_id)
        except JobPost.DoesNotExist:
            return Response({"message":"Job Post does not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = JobPostSerializer(job_post)
        return Response({"data":serializer.data}, status=status.HTTP_302_FOUND)
    
    else:
        return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
# get all job post by all colleges using api decorators.
@api_view(['GET'])
@csrf_exempt
def get_job_posts_list(request):
    if request.method == 'GET':
        try:
            job_post_list = JobPost.objects.all()
            pagination_class = CustomPagination()
            result_page = pagination_class.paginate_queryset(job_post_list, request)
            serializer = JobPostSerializer(result_page, many=True)
            return pagination_class.get_paginated_response(serializer.data)
        except JobPost.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
