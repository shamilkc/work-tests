from django.contrib import admin 
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display =['name','email','is_approved']

admin.site.register(Profile,ProfileAdmin)
