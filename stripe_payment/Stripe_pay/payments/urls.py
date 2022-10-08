from django.urls import path

from . import views

urlpatterns = [
    path('cancel/', views.CancelView, name='cancel'),
    path('success/', views.SuccessView, name='success'),
    path('create-checkout-session/', views.CreateCheckoutSessionView, name='create-checkout-session')
]