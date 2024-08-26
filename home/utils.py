from home.models import Student
import time
from django.core.mail import send_mail
from django.conf import settings

def run_this_function():
    print("Function Started")
    
    time.sleep(2)
    
    print("Function Executed")
    
def send_email_to_client():
    subject = "TEst MEssage"
    message = "From django test message hai ye ok"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["mujtabazaidi0512@gmail.com"]
    

    send_mail(subject, message, from_email, recipient_list)