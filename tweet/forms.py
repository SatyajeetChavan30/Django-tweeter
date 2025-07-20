from django import forms
from .models import tweet, contact_me
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class tweetFrom(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text', 'photo']

class UserRgistrationForm(UserCreationForm):
    email = forms.CharField( max_length=50)
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')
        
class contactFORM(forms.ModelForm):
    class Meta:
        model = contact_me
        fields = ['name', 'email', 'text']