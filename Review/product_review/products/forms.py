from django import forms
from . models import *

class Reviewforms(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','title','description']