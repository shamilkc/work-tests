from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms



class myUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=500)
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2','age','phone','address']



