from django.shortcuts import render,redirect
from django.conf import settings
import requests
# Create your views here.

def home(request):
    context= {}
    
    if request.method == "POST":
        number = request.POST['phone']
        message = request.POST['msg']
        headers = {"Authorization":settings.WHATSAPP_TOKEN}
        payload = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": "91"+number,
                    "type": "text",
                    "text": {
                        "preview_url": False,
                        "body": message
                    }
                    }

        response = requests.post(settings.WHATSAPP_URL,headers=headers,json=payload).json()
        context = {"response":response}
        redirect("home")
        
    return render(request,'home.html',context)