from django.shortcuts import render

def home(request):
    return render(request,'base.html')


def successPage(request):
    return render(request,'success.html')
