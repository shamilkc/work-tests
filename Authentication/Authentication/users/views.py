

from turtle import delay
from django.http import HttpResponse
from . models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import myUserCreationForm
from .tasks import email_send,email_send_user





def home(request):
    users_for_approvel = Profile.objects.filter(is_approved = False)

    return render(request,'index.html',{'users':users_for_approvel})



def login_user(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['pass']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"user does not exist")
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            approve = Profile.objects.get(user=user)
            if approve.is_approved == True:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"This user is waiting for admin approvel")
        else:
             messages.error(request,"user name or password does not exist")
             
    return render(request,'login.html',{'page':page})


def registerUser(request):
    
    form = myUserCreationForm()
    if request.method == "POST":
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username = user.username.lower()
            age = user.age = form.cleaned_data.get('age')
            email = user.age = form.cleaned_data.get('email')
            address = user.address = form.cleaned_data.get('address')
            phone = user.phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user =User.objects.create(email=email,username=username)
            user.set_password(password)

            
            user.save()
            messages.success(request,"Registration success!you can login once admin approved you")

            email_send.delay(email)

            profile = Profile(user=user,name=username,age=age,email=email,address=address,phone=phone)
            profile.save()
            
            return redirect('home')
        else:
            messages.error(request,' Error enterd data is invalid')
    return render(request,'login.html',{'form':form})


def logout_user(request):
    logout(request,)
    return redirect('home')


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)

    context = {
        'profile':profile
    }
    return render(request,'profile.html',context)


def activateAccount(request):
    messages.error(request,"login as admin to approve this user")

    return redirect('login')


def approveUser(request,pk):
    user = Profile.objects.get(id=pk)
    user.is_approved = True
    user.save()
    email = user.email
    email_send_user.delay(email)
    return redirect('home')


def disApproveUser(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('home')