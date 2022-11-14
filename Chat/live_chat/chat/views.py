from django.shortcuts import render


# Create your views here.

def chat(request):
    user = request.user
    return render(request,'chat/chat.html',{'user':user})