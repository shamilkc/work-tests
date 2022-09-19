from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout 

@api_view(['POST'])
def regUser(request):
    if request.method =='POST':
        username = request.data['username']
        password = request.data['password']
        user = User(username=username,password=password)
        user.set_password(password)
        user.save()
        refresh =RefreshToken.for_user(user)
    return Response({
        'status':'success',
        
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        })


# @api_view(['POST'])
# def loginUser(request):
#     if request.method =='POST':
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username,password=password)


#     return Response({'status:success'})

