from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo



@api_view(['GET'])
def getRoutes(request):
    routes =[
        'api/',
        'api/show',
        'api/show/<id>/',
        
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request):
    notes = Todo.objects.all()
    serializer = TodoSerializer(notes,many =True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showItem(request,pk):
    notes = Todo.objects.get(id=pk)
    serializer = TodoSerializer(notes,many =False)
    return Response(serializer.data)

