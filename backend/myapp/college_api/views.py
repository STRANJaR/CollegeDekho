from django.shortcuts import render, redirect
from myapp.models import College, Subject_Teacher, College_Profile, CollegePasswordResetToken
from .serializers import CollegeSerializer, CollegeProfileSerializer, SubjectTeacherSerializer, CollegePasswordResetTokenSerializer
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


# Creating signup api for college using api_view decorator
@api_view(['POST'])
@csrf_exempt
def college_signup(request): 
    user_email = request.data.get('email')     #fetching user email.
    # request.data._mutable = True   #with this code queryset converted into mutable form
    data = request.data    #storing all sended data in data variable
    data = data.copy()    #make a copy of data in data variable.
    hashed_password = make_password(data.get('password'))  # hashing password
    data['password'] = hashed_password         #updating old password with hashed password
    serializer = CollegeSerializer(data=data)
    
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
          
    
        return Response({"message":"Your signup is done successfuly", "serialized data":serializer.data}, status=status.HTTP_201_CREATED)
    
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
    except College_Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = CollegeProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    



# forget_password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def forget_password(request):
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
        return Response({"error":"token is not saved in database."})
    
    
    subject = 'Forget Password Request.'
    body = f'Please click the following link to reset your password: http://127.0.0.1:8000/reset_password/{token}'
    sender_email = 'yadav.parishram@gmail.com'  # email id of sender mail
    recipient_email = user_email

    # Send email
    send_mail(subject, body, sender_email, [recipient_email], fail_silently=False,)
    
    return Response({"message":"reset password mail is send successfully to the given mail."}, status=status.HTTP_201_CREATED)   



# reset password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def reset_password(request, token):
    
    try:
        new_password = request.data.get('new_password')
    
    except:
        return Response({"error":"Please enter new password..."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        reset_token_object = CollegePasswordResetToken.objects.get(token=token)
    except:
        return Response({"error":"user not exits with this token..."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if reset_token_object.is_expired():
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        hashed_new_password = make_password(new_password)    #hashing password
        user = reset_token_object.user                      #get user from reset_token_object
        user_data = College.objects.get(id=user.id)         #get user data using user_id 
        
        user_data.password = hashed_new_password           #saving hashed password to main password
        user_data.save()                                   #saving new password to password
        reset_token_object.delete()                       #deleting reset_token_object from token object..
        return Response({"message":"your password is reset successfully..."})
        
    except CollegePasswordResetToken.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
