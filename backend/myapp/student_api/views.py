from django.shortcuts import render, redirect
from myapp.models import Student, StudentPasswordResetToken
from .serializers import StudentSerializer, StudentPasswordResetTokenSerializer 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from myapp.pagination import CustomPagination
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import secrets
from myapp.validation import validate_signup_data



# creating a signup api for Student using api_view 
@api_view(['POST'])
@csrf_exempt
def student_signup(request):
    # if request.user.is_authenticated:
    user_email = request.data.get('email')     #fetching user email.
    # request.data._mutable = True   #with thid code queryset converted into mutable form
    data = request.data    #storing all sended data in data variable
    data = data.copy()    #make a copy of data in data variable.
    hashed_password = make_password(data.get('password'))  # hashing password
    data['password'] = hashed_password         #updating old password with hashed password
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        
        # validating username using own validation function.
        validate_signup_data(serializer.validated_data, Student)
        
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
          
        return Response({"message":"Your signup is done successfull", "serializer data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    


# Creating login api for Student using api_view decorator
@api_view(['POST'])
@csrf_exempt
def student_login(request):
    # if request.user.is_authenticated:
        if not request.user.is_authenticated:
            username = request.data.get('username')
            password = request.data.get('password')
            print(username)
            print(password)
            user = Student.objects.get(username=username, password=password)
            if user:
                return Response({'message': 'Login successful', 'user': StudentSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("You are already Logged In.")
    
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)



# forget_password api using api_view decorator with function based view.
@api_view(['POST'])
@csrf_exempt
def forget_password(request):
    user_email = request.data.get('email')
    
    try:
        user = Student.objects.get(email = user_email)
        print(user.id)
    except Student.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # generate token using secret module.
    token = secrets.token_urlsafe(25)
    
    try:
        StudentPasswordResetToken.objects.create(user=user, token=token)
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
        print(new_password)
    except:
        return Response({"error":"Please enter new password..."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        reset_token_object = StudentPasswordResetToken.objects.get(token=token)
    except:
        return Response({"error":"user not exits with this token..."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if reset_token_object.is_expired():
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        hashed_new_password = make_password(new_password)
        user = reset_token_object.user
        user_data = Student.objects.get(id=user.id)
        
        user_data.password = hashed_new_password
        user_data.save()
        reset_token_object.delete()
        return Response({"message":"your password is reset successfully..."})
        
    except StudentPasswordResetToken.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
