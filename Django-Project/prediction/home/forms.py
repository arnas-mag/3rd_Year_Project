from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create user form 

class NewUserForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'first_name',
            'placeholder':('First Name')
        }
    ))
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'last_name',
            'placeholder':('Last Name')
        }
    ))
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'email',
            'placeholder':('Email')
        }
    ))
    
    password1 = forms.CharField(max_length=16,widget=forms.TextInput(
        attrs={
            #'type':'first_name',
            'placeholder':('Password')
        }
    ))
    
    password2 = forms.CharField(max_length=16,widget=forms.TextInput(
        attrs={
            #'type':'first_name',
            'placeholder':('Repeat Password')
        }
    ))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password1', 'password2']