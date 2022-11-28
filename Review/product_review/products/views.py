from django.shortcuts import render,redirect
from .models import Products,Review
from .forms import Reviewforms
# Create your views here.

def product(request,pk):
    url = request.META.get('HTTP_REFERER')
    product = Products.objects.get(id=pk)
    product_reviews = Review.objects.filter(product__id=pk).order_by('-updated')
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(user__id=request.user.id,product__id=pk)
            form = Reviewforms(request.POST,instance=reviews)
            form.save()
            return redirect(url)

        except Review.DoesNotExist:
            form= Reviewforms(request.POST)
            if form.is_valid():
                data =  Review()
                data.title = form.cleaned_data['title']
                data.rating = form.cleaned_data['rating']
                data.description= form.cleaned_data['description']
                data.product_id = pk
                data.user_id = request.user.id
                data.save()
                return redirect(url)

    context = {
        'product':product,
        'product_reviews':product_reviews
    }
    return render(request,'products/product.html',context)


