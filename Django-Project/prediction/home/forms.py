from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create user form 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #first_name = forms.CharField(widget=forms.TextInput(
     #   attrs={
      #      'type':'first_name',
       #     'placeholder':('First Name')
        #}
    #))
    
    #last_name = forms.CharField(widget=forms.TextInput(
    #    attrs={
    #        'type':'last_name',
    #        'placeholder':('Last Name')
    #    }
    #))
    
    #email = forms.CharField(widget=forms.TextInput(
    #    attrs={
    #        'type':'email',
    #        'placeholder':('Email')
    #    }
    #))
    
    #password1 = forms.CharField(max_length=16,widget=forms.TextInput(
    #    attrs={
    #        #'type':'first_name',
    #        'placeholder':('Password')
    #    }
    #))
    
    #password2 = forms.CharField(max_length=16,widget=forms.TextInput(
    #    attrs={
    #        #'type':'first_name',
    #        'placeholder':('Repeat Password')
    #    }
    #))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user