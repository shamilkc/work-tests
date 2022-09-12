
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('userprofile/<str:pk>/',views.userProfile,name="profile"),
    path('activate/',views.activateAccount,name="activate"),
    path('approve-user/<str:pk>/',views.approveUser,name="approve"),
    path('disapproveuser/<str:pk>/',views.disApproveUser,name="disapprove"),
    
]