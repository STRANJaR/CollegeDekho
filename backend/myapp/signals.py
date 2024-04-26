from django.utils import timezone
from myapp.models import College
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.dispatch import Signal, receiver
from datetime import datetime, timedelta


# creating custom user_login_failed signals.
user_login_failed = Signal()

# blocked user detailed.
user_blocked = Signal()

# response_signal = Signal()


BLOCK_DURATION = timedelta(minutes=2)
MAX_LOGIN_ATTEMPTS = 3
login_attempts = {}


# user login failed signal.
@receiver(user_login_failed)
def handle_failed_login(sender, credentials, request, **kwargs):
    username = credentials.username     #here crendeials is user object
    user = sender.objects.get(username=username)
    print("user:",  user)
    print(sender)
    
    # Get the user's failed login attempts
    failed_attempt = user.failed_login_attempts
    print(failed_attempt)
    
    if failed_attempt < MAX_LOGIN_ATTEMPTS:
        user.is_active = True
        user.failed_login_attempts += 1
        user.save()
        
        return Response({"message":"Try Again With Valid Credentials"})
    
    else:
        user.failed_login_attempts = 0
        user.locked_until = datetime.now() + BLOCK_DURATION
        user_blocked.send(sender=College, username=username, block_duration=BLOCK_DURATION)
        user.is_active = False
        user.save()
        response_data = {"message": "This is a response from the signal"}
        # response_signal.send(sender=None, response_data=response_data)
        return Response({"message": "User is blocked for {BLOCK_DURATION} minutes"}, status=status.HTTP_403_FORBIDDEN)



    
    

