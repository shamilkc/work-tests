from django.shortcuts import render
import razorpay 
# Create your views here.

def home(request):
    
    amount = 50000
    client =razorpay.Client(auth=('rzp_test_S4gKRF9GWSK1nB','Q4SIaGnKtZUzKGMKgPILVxid'))

    payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    print(payment)
    return render(request,'home.html',{'payment':payment})

    
