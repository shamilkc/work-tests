from django.shortcuts import render
from products.models import Products,Review
# Create your views here.

def home(request):
    products = Products.objects.all()

    context = {
        'products':products
    }
    return render(request,'home.html',context)