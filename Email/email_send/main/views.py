from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from email.mime.image import MIMEImage
from pathlib import Path
from django.template.loader import render_to_string



def home(request):
    if request.method =="POST":

        image_path = 'static/img/post-1.jpg'
        image_name = Path(image_path).name

        context = {'image_name':image_name}

        html_content = render_to_string('email.html', context=context).strip()

        subject = 'HTML Email'
        recipients = [request.POST['email']]
        sender = settings.EMAIL_HOST_USER

        msg = EmailMultiAlternatives(subject, html_content, from_email=sender, to=recipients)
        msg.content_subtype = 'html'  # Main content is text/html
        msg.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!

       
        # Create an inline attachment
        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', '<{}>'.format(image_name))
            msg.attach(image)

       
        msg.send()

        return redirect('home')
    return render(request,'home.html') 
   