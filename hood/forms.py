from django.contrib.auth.models import User
from django import forms
from .models import Neighbourhood,User,Businesses,Post 


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['hood_name','location','occupants']



class BusinessForm(forms.ModelForm):
    class Meta:
        model= Businesses
        fields = ['logo','business_name','business_email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','address']