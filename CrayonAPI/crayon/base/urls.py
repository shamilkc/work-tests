from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('get-organizations/',views.getOrganizations,name="get-organizations"),
    path('get-users/',views.getUsers,name="get-users"),
    path('get-cusomer-tenent/',views.getCusomerTenent,name="getcusomertenent"),
    path('get-a-cusomer-tenent/',views.getSingleCusomerTenent,name="getsinglecusomertenent"),
    path('create-cusomer-tenent/',views.createCusomerTenet,name="createcusomertenent"),
    ]