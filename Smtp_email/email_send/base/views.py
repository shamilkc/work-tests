from django.shortcuts import render
from email.message import EmailMessage
import smtplib

# Create your views here.

def home(request):
    if request.method == 'POST':
        # Get form data
        to_email = request.POST['to_email']
        smtp_server = request.POST['smtp_server']
        smtp_port = int(request.POST['smtp_port'])
        smtp_username = request.POST['smtp_username']
        smtp_password = request.POST['smtp_password']
        subject = request.POST['subject']
        message = request.POST['message']
        # Create message object
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = to_email
        print("got data")
        try:
            # Connect to SMTP server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                print("connection success")
                # Send message
                server.send_message(msg)
                print("email send")
            return render(request, 'success.html')
        except:
            return render(request, 'error.html')
    return render(request,'home.html')