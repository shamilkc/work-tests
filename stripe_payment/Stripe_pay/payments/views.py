
from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from django.shortcuts import redirect


stripe.api_key = settings.STRIPE_SECRET_KEY


def CreateCheckoutSessionView(request):

    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    
                    'price': 'price_1LqVL1SGaPgu566PNa6k4r4j',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL+ '/payments/success',
            cancel_url=settings.BASE_URL + '/payments/cancel',
            )
        return redirect(checkout_session.url, code=303)













 
   




def SuccessView(request):
    return render(request,"success.html",)


def CancelView(request):
    return render(request,"cancel.html",)



def HomePageView(request):
    return render(request,"home.html",)