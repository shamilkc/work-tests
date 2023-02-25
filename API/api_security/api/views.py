from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from base.models import Blog
from .serializers import BlogSerializer



@api_view(['GET'])
@permission_classes([AllowAny])
def apiRoutes(request):
    api_urls = [
        {
        'Create new user':'create-user/',
        'Login user':'login-user/',
        'update user':'update-user/',
        'Generate Token for existing user':'token/',
        'Generate Access Token':'token/refresh/',
        
    },
        {
        'List all Blogs':'blogs/',
        'Show  Blog':'blog/<id>/',
        'Create a blog':'create/',
        'Update a blog':'blog/<id>/update/',
        'Delete a blog':'blog/<id>/delete/',
    }
    ]
    return Response(api_urls)



#user api

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    #creating user with a username and password
    if User.objects.filter(username=request.data['username']).exists():
        return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )

    refresh_token = RefreshToken.for_user(user=user)
    return Response(
        {"message": "User created successfully", "refresh": str(refresh_token), "access":str(refresh_token.access_token)
        }, 
    status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    #updating user
    user = User.objects.get(username=str(pk))
    
    user.username = request.data.get('username', user.username)
    user.set_password(request.data.get('password', user.password))
    user.save()
    return Response({"message": "User updated successfully"})



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    #login a user and returning the token
    username = request.data['username']
    password = request.data['password']
    
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        refresh_token = RefreshToken.for_user(user=user)
        return Response({"message": "logged successfully", "refresh": str(refresh_token), "access":str(refresh_token.access_token)
        },)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



#blogs api

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showBlog(request,pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog,many=False)

    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createBlog(request):
    serializer = BlogSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("data is not valid")
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBlog(request,pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("data is not valid")
    return Response(serializer.data)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBlog(request,pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response("Item deleted")
