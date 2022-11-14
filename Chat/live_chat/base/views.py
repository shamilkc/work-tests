from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
       
        
    return render(request,'base/home.html')



def logoutview(request):
    logout(request)
    return redirect('home')