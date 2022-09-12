
from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.IntegerField(null=True)
    is_approved = models.BooleanField(default=False)
   
    

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='profile')
    
    
   

    def __str__(self):
        return self.name



   
   


   

 

