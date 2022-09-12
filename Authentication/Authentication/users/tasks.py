
from celery import shared_task
from email import message
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from Authentication import settings






@shared_task
def email_send(email):
    subject = "Account activation request"
    message = f'A user with email {email} has sent account activation request http://127.0.0.1:8000/activate/'
    to_email = 'muhammedshamil299@gmail.com'
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,
    recipient_list=[to_email],fail_silently=True)
    
    return "Done"


@shared_task
def email_send_user(email):
    subject = "Account activation request accepted"
    message = f'Your account activation request  has accepted by the admin. login here: http://127.0.0.1:8000/login/'
    to_email = email
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,
    recipient_list=[to_email],fail_silently=True)
    
    return "Done"
