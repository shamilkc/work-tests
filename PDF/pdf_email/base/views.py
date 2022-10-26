from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from . models import Files

# Create your views here.

def home(request):
    
    if request.method =="POST":

        html_content = render_to_string('email.html', ).strip()

        subject = 'PDF ATTACHMENT'
        recipients = [request.POST['email']]
        sender = settings.EMAIL_HOST_USER
        file = request.FILES['file']

        

        msg = EmailMessage(subject, html_content, from_email=sender, to=recipients)
        msg.content_subtype = 'html'  
        # msg.mixed_subtype = 'related'  
        
        msg.attach(file.name,file.read(),file.content_type)
        msg.send()

        file_save = Files(file=file)
        file_save.save()
        
        return redirect('home')
    return render(request,'home.html')




def email(request):
    file = Files.objects.get(id=1)
    path = file.file.path
    if request.method =="POST":

        html_content = render_to_string('email.html', ).strip()

        subject = request.POST['subject']
        recipients = [request.POST['email']]
        sender = settings.EMAIL_HOST_USER

        msg = EmailMessage(subject, html_content, from_email=sender, to=recipients)
        msg.content_subtype = 'html'  
        # msg.mixed_subtype = 'related' 

        msg.attach_file(path)
        msg.send()

        return redirect('email')
    return render(request,'emailview.html')
